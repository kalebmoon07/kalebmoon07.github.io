#!/usr/bin/env python3
"""Sync homepage content from the LaTeX CV repository."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


BEGIN_MARKER = "<!-- BEGIN AUTO-SYNC: {name} -->"
END_MARKER = "<!-- END AUTO-SYNC: {name} -->"


def strip_latex_comments(text: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines())


def read_braced(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"Expected '{{' at index {start}")
    depth = 0
    out: list[str] = []
    i = start
    while i < len(text):
        ch = text[i]
        if ch == "{" and (i == 0 or text[i - 1] != "\\"):
            depth += 1
            if depth > 1:
                out.append(ch)
        elif ch == "}" and (i == 0 or text[i - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return "".join(out), i + 1
            out.append(ch)
        else:
            out.append(ch)
        i += 1
    raise ValueError("Unterminated braced block")


def extract_macro_args(text: str, macro_name: str, arg_count: int) -> list[tuple[list[str], int, int]]:
    matches: list[tuple[list[str], int, int]] = []
    needle = f"\\{macro_name}"
    pos = 0
    while True:
        start = text.find(needle, pos)
        if start == -1:
            break
        idx = start + len(needle)
        args: list[str] = []
        while len(args) < arg_count:
            while idx < len(text) and text[idx].isspace():
                idx += 1
            arg, idx = read_braced(text, idx)
            args.append(arg)
        matches.append((args, start, idx))
        pos = idx
    return matches


def latex_to_text(value: str) -> str:
    text = strip_latex_comments(value).strip()
    replacements = {
        r"\ProfLee{}": "<sup>[KL]</sup>",
        r"\ProfLee": "<sup>[KL]</sup>",
        r"\TeachingGrad{}": "(G)",
        r"\TeachingGrad": "(G)",
        r"\TeachingUndergrad{}": "(U)",
        r"\TeachingUndergrad": "(U)",
        r"\&": "&",
        r"\%": "%",
        r"\_": "_",
        r"\#": "#",
        r"\newline": "; ",
        r"\\": "; ",
        "~": " ",
        r"\nopagebreak": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"\\([&%_#$])", r"\1", text)
    text = re.sub(r"\\href\{([^{}]+)\}\{([^{}]+)\}", r"[\2](\1)", text)
    text = re.sub(r"\\(?:textbf|textit|emph|texttt|mathrm|operatorname)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\textsuperscript\{([^{}]*)\}", r"<sup>\1</sup>", text)
    text = re.sub(r"\\llap\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\begin\{[^{}]+\}|\\end\{[^{}]+\}", "", text)
    text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^\]]*\])?", "", text)
    accent_patterns = {
        r"\{\\'([A-Za-z])\}": r"\1",
        r"\{\\`([A-Za-z])\}": r"\1",
        r"\{\\~([A-Za-z])\}": r"\1",
        r"\{\\\^([A-Za-z])\}": r"\1",
        r"\{\\c\s*([A-Za-z])\}": r"\1",
        r"\{\\v\s*([A-Za-z])\}": r"\1",
    }
    for pattern, repl in accent_patterns.items():
        text = re.sub(pattern, repl, text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("--", "–")
    text = re.sub(r"\s+", " ", text)
    return text.strip(" ,;")


def parse_item_list(value: str) -> list[str]:
    clean = strip_latex_comments(value)
    items = re.findall(r"\\item\s+(.+?)(?=(?:\\item\b|\\end\{cvitems\}|$))", clean, flags=re.S)
    parsed = [latex_to_text(item) for item in items]
    return [item for item in parsed if item]


def split_sections(text: str, macro_name: str, arg_count: int) -> list[dict[str, Any]]:
    matches = extract_macro_args(text, macro_name, arg_count)
    sections: list[dict[str, Any]] = []
    for index, (args, start, end) in enumerate(matches):
        content_end = matches[index + 1][1] if index + 1 < len(matches) else len(text)
        sections.append(
            {
                "title": latex_to_text(args[0]),
                "subtitle": latex_to_text(args[1]) if arg_count > 1 else "",
                "raw_title": args[0],
                "content": text[end:content_end],
                "start": start,
                "end": end,
            }
        )
    return sections


def slugify(value: str) -> str:
    ascii_text = (
        latex_to_text(value)
        .replace("&", "and")
        .replace("<sup>[KL]</sup>", "kl")
        .lower()
    )
    ascii_text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", ascii_text)
    ascii_text = re.sub(r"[^a-z0-9]+", "-", ascii_text)
    return ascii_text.strip("-") or "item"


MONTH_MAP = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def infer_year(*values: str) -> str:
    for value in values:
        match = re.search(r"(19|20)\d{2}", value)
        if match:
            return match.group(0)
    return "1900"


def normalize_publication_date(year_text: str) -> str:
    year = infer_year(year_text)
    return f"{year}-01-01"


def normalize_talk_date(title: str, display_date: str) -> str:
    clean = display_date.replace("–", "-")
    explicit = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2}),\s*(\d{4})", clean)
    if explicit:
        month, day, year = explicit.groups()
        return f"{year}-{MONTH_MAP[month]:02d}-{int(day):02d}"

    partial = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2})", clean)
    if partial:
        month, day = partial.groups()
        year = infer_year(clean, title)
        return f"{year}-{MONTH_MAP[month]:02d}-{int(day):02d}"

    year = infer_year(clean, title)
    return f"{year}-01-01"


def normalize_teaching_date(display_date: str) -> str:
    clean = display_date.strip()
    season = re.search(r"(Spring|Summer|Fall|Winter)\s+((?:19|20)\d{2})", clean, flags=re.I)
    if season:
        term, year = season.groups()
        month = {
            "spring": 3,
            "summer": 6,
            "fall": 9,
            "winter": 12,
        }[term.lower()]
        return f"{year}-{month:02d}-01"
    year = infer_year(clean)
    return f"{year}-01-01"


def compact_date_token(date_text: str) -> str:
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})$", date_text)
    if not match:
        return "000000"
    year, month, day = match.groups()
    return f"{year[2:]}{month}{day}"


def extract_event_slug(item: dict[str, Any]) -> str:
    title = item.get("title", "").strip()
    if title:
        if item.get("talk_type") == "seminar":
            title = re.sub(r"^research\s+talk\s+at\s+", "", title, flags=re.I)
        return slugify(title)
    event = item.get("event", "").strip()
    if event:
        return slugify(event)
    return "event"


def extract_course_id(title: str, course_url: str) -> str:
    if course_url:
        match = re.search(r"/teaching/([^/]+)/", course_url)
        if match:
            return slugify(match.group(1))

    clean_title = re.sub(r"^\((?:G|U)\)\s*", "", title).strip()
    words = re.findall(r"[A-Za-z0-9]+", clean_title)
    significant = [word for word in words if word.lower() not in {"and", "for", "of", "the"}]
    acronym = "".join(word[0].lower() for word in significant if word)
    if len(acronym) >= 2:
        return acronym
    return slugify(clean_title) or "course"


def talk_type_slug(talk_type: str) -> str:
    return {
        "conference_international": "conf-intl",
        "conference_domestic": "conf-dom",
        "seminar": "seminar",
    }.get(talk_type, slugify(talk_type))


def teaching_type_slug(teaching_type: str) -> str:
    return {
        "assistant": "TA",
        "lecturer": "lecturer",
    }.get(teaching_type, slugify(teaching_type))


def yaml_scalar(value: Any) -> str:
    if value is None or value == "":
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def dump_yaml_value(lines: list[str], key: str, value: Any, indent: int = 0) -> None:
    prefix = " " * indent
    if isinstance(value, list):
        if not value:
            lines.append(f"{prefix}{key}: []")
            return
        lines.append(f"{prefix}{key}:")
        for item in value:
            if isinstance(item, dict):
                lines.append(f"{prefix}  -")
                for sub_key, sub_value in item.items():
                    dump_yaml_value(lines, sub_key, sub_value, indent + 4)
            else:
                lines.append(f"{prefix}  - {yaml_scalar(item)}")
        return
    lines.append(f"{prefix}{key}: {yaml_scalar(value)}")


def write_collection_item(directory: Path, filename: str, frontmatter: dict[str, Any], body: str = "") -> None:
    lines = ["---"]
    for key, value in frontmatter.items():
        dump_yaml_value(lines, key, value)
    lines.append("---")
    if body:
        lines.append(body.rstrip())
    lines.append("")
    directory.mkdir(parents=True, exist_ok=True)
    (directory / filename).write_text("\n".join(lines), encoding="utf-8")


def load_local_sync_config(homepage_root: Path) -> dict[str, Any]:
    config_path = homepage_root / ".tmp" / "sync_from_resume.local.json"
    if not config_path.exists():
        return {}
    return json.loads(config_path.read_text(encoding="utf-8"))


def save_local_sync_config(homepage_root: Path, resume_root: Path) -> None:
    config_path = homepage_root / ".tmp" / "sync_from_resume.local.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        json.dumps({"resume_repo": str(resume_root)}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def reset_generated_collection(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for path in directory.glob("*.md"):
        path.unlink()


def replace_marked_section(path: Path, name: str, new_content: str) -> None:
    begin = BEGIN_MARKER.format(name=name)
    end = END_MARKER.format(name=name)
    original = path.read_text(encoding="utf-8")
    replacement = f"{begin}\n{new_content.rstrip()}\n{end}"
    if begin in original and end in original:
        updated = re.sub(
            re.escape(begin) + r".*?" + re.escape(end),
            replacement,
            original,
            count=1,
            flags=re.S,
        )
    else:
        updated = original.rstrip() + "\n\n" + replacement + "\n"
    path.write_text(updated, encoding="utf-8")


def load_exported_publications(resume_root: Path, homepage_root: Path) -> dict[str, Any]:
    exporter = resume_root / "automation" / "export_publications.py"
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    result = subprocess.run(
        [sys.executable, str(exporter), "--repo-root", str(resume_root), "--format", "json"],
        cwd=homepage_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        check=True,
    )
    return json.loads(result.stdout)


def parse_proj_entries(path: Path) -> list[dict[str, Any]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    entries = []
    for args, _, _ in extract_macro_args(text, "projentry", 4):
        entries.append(
            {
                "title": latex_to_text(args[0]),
                "organization": latex_to_text(args[1]),
                "date": latex_to_text(args[2]),
                "details": parse_item_list(args[3]),
            }
        )
    return entries


def parse_education(path: Path) -> list[dict[str, Any]]:
    return parse_proj_entries(path)


def parse_skills(path: Path) -> list[dict[str, Any]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    skills = []
    for args, _, _ in extract_macro_args(text, "cvskill", 2):
        keywords = [item.strip() for item in latex_to_text(args[1]).split(",") if item.strip()]
        skills.append({"name": latex_to_text(args[0]), "keywords": keywords})
    return skills


def parse_research_interests(path: Path) -> list[dict[str, str]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    interests = []
    for bold, description in re.findall(r"\\item\s+\\textbf\{([^{}]+)\}:\s*(.+?)(?=(?:\\item\b|$))", text, flags=re.S):
        interests.append({"topic": latex_to_text(bold), "details": latex_to_text(description)})
    return interests


def parse_activities(path: Path) -> list[dict[str, str]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    return [
        {"name": latex_to_text(args[0]), "date": latex_to_text(args[1])}
        for args, _, _ in extract_macro_args(text, "activityEntry", 2)
    ]


def parse_projects(path: Path) -> dict[str, list[dict[str, Any]]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    sections = split_sections(text, "cvsection", 2)
    data = {
        "leader_research": [],
        "researcher_research": [],
        "researcher_industry": [],
    }
    for section in sections:
        role = "leader" if "leader" in section["title"].lower() else "researcher"
        subsections = split_sections(section["content"], "cvsubsection", 1)
        for subsection in subsections:
            target = (
                "leader_research"
                if role == "leader"
                else "researcher_industry"
                if "industry" in subsection["title"].lower()
                else "researcher_research"
            )
            macro_name = "projFundIndustryEntry" if "industry" in subsection["title"].lower() else "projFundEntry"
            for args, _, _ in extract_macro_args(subsection["content"], macro_name, 4):
                data[target].append(
                    {
                        "title": latex_to_text(args[0]),
                        "sponsor": latex_to_text(args[1]),
                        "date": latex_to_text(args[2]),
                        "details": parse_item_list(args[3]),
                    }
                )
    return data


def parse_presentations(path: Path) -> list[dict[str, Any]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    talks = []
    for subsection in split_sections(text, "cvsubsection", 1):
        if "international" in subsection["title"].lower():
            talk_type = "conference_international"
        elif "domestic" in subsection["title"].lower():
            talk_type = "conference_domestic"
        else:
            talk_type = "seminar"
        for order, (args, _, _) in enumerate(extract_macro_args(subsection["content"], "ptentry", 5), start=1):
            talks.append(
                {
                    "title": latex_to_text(args[0]),
                    "event": latex_to_text(args[1]),
                    "location": latex_to_text(args[2]),
                    "date": latex_to_text(args[3]),
                    "display_date": latex_to_text(args[3]),
                    "talk_type": talk_type,
                    "items": parse_item_list(args[4]),
                    "subsequence": order,
                }
            )
    total = len(talks)
    for index, talk in enumerate(talks):
        talk["sequence"] = total - index
    return talks


def parse_teaching(path: Path) -> list[dict[str, Any]]:
    text = strip_latex_comments(path.read_text(encoding="utf-8"))
    entries = []
    for subsection in split_sections(text, "cvsubsection", 1):
        teaching_type = "lecturer" if "lecturer" in subsection["title"].lower() else "assistant"
        for order, (args, _, _) in enumerate(extract_macro_args(subsection["content"], "teachingentry", 4), start=1):
            title_arg = args[0]
            course_url = None
            href_match = re.search(r"\\href\{([^{}]+)\}\{([^{}]+)\}", title_arg)
            if href_match:
                course_url = href_match.group(1)
            title_text = latex_to_text(re.sub(r"\\href\{([^{}]+)\}\{([^{}]+)\}", r"\2", title_arg))
            entries.append(
                {
                    "title": title_text,
                    "institution": "POSTECH",
                    "date": latex_to_text(args[3]),
                    "display_date": latex_to_text(args[3]),
                    "teaching_type": teaching_type,
                    "evaluation": latex_to_text(args[1]),
                    "attendees": latex_to_text(args[2]),
                    "course_url": course_url or "",
                    "subsequence": order,
                }
            )
    total = len(entries)
    for index, entry in enumerate(entries):
        entry["sequence"] = total - index
    return entries


def render_detail_list(items: list[str], indent: str = "  ") -> list[str]:
    lines = []
    for item in items:
        lines.append(f"{indent}* {item}")
    return lines


def render_about_block(interests: list[dict[str, str]], work: list[dict[str, Any]], awards: list[dict[str, Any]], activities: list[dict[str, str]]) -> str:
    lines = ["## Research Interests", ""]
    for interest in interests:
        lines.append(f"* **{interest['topic']}**: {interest['details']}")
    lines.extend(["", "## Work Experience", ""])
    for item in work:
        lines.append(f"* **{item['title']}**, {item['organization']} ({item['date']})")
        lines.extend(render_detail_list(item["details"]))
    lines.extend(["", "## Awards", ""])
    for award in awards:
        lines.append(f"* **{award['title']}**, {award['organization']} ({award['date']})")
        lines.extend(render_detail_list(award["details"]))
    lines.extend(["", "## Academic Activities", "", "### Journal Reviewer", ""])
    for activity in activities:
        lines.append(f"* {activity['name']} ({activity['date']})")
    return "\n".join(lines).rstrip()


def render_projects_block(projects: dict[str, list[dict[str, Any]]]) -> str:
    lines = ["## As a project leader", "", "### Research Projects", ""]
    for project in projects["leader_research"]:
        lines.append(f"* **{project['title']}** ({project['date']})")
        lines.append(f"  * {project['sponsor']}")
        for detail in project["details"]:
            if "grant" in detail.lower():
                continue
            lines.append(f"  * {detail}")
    lines.extend(["", "## As a researcher/student at POSTECH", "", "(<sup>[KL]</sup>: Prof. Kangbok Lee is the PI)", "", "### Research Projects", ""])
    for project in projects["researcher_research"]:
        lines.append(f"* **{project['title']}** ({project['date']})")
        lines.append(f"  * {project['sponsor']}")
        for detail in project["details"]:
            lines.append(f"  * {detail}")
    lines.extend(["", "### Industry Projects", ""])
    for project in projects["researcher_industry"]:
        lines.append(f"* **{project['title']}** ({project['date']})")
        lines.append(f"  * {project['sponsor']}")
        for detail in project["details"]:
            lines.append(f"  * {detail}")
    return "\n".join(lines).rstrip()


def render_cv_block(work: list[dict[str, Any]], skills: list[dict[str, Any]]) -> str:
    lines = ["Work experience", "======"]
    for item in work:
        lines.append(f"* **{item['title']}**, {item['organization']} ({item['date']})")
        lines.extend(render_detail_list(item["details"]))
        lines.append("")
    lines.extend(["Skills", "======"])
    for skill in skills:
        lines.append(f"* {skill['name']}: {', '.join(skill['keywords'])}")
    return "\n".join(lines).rstrip()


def sync_collections(homepage_root: Path, publications: list[dict[str, Any]], patents: list[dict[str, Any]], talks: list[dict[str, Any]], teaching: list[dict[str, Any]]) -> None:
    publications_dir = homepage_root / "_publications"
    talks_dir = homepage_root / "_talks"
    teaching_dir = homepage_root / "_teaching"
    reset_generated_collection(publications_dir)
    reset_generated_collection(talks_dir)
    reset_generated_collection(teaching_dir)

    for item in publications + patents:
        slug = f"{slugify(item['source_key'])}.md"
        write_collection_item(
            publications_dir,
            slug,
            {
                "title": item["title"],
                "authors": [author["name"] for author in item["authors"]],
                "venue": item["venue"],
                "date": normalize_publication_date(item["year"]),
                "display_date": item["year"],
                "pub_type": item["group"],
                "paperurl": item["paperurl"],
                "doi": item.get("doi", ""),
                "citation": item["citation"],
                "source_key": item["source_key"],
                "sequence": item["sequence"],
                "group_title": item["group_title"],
                "notes": item.get("notes", []),
            },
        )

    for item in talks:
        normalized_date = normalize_talk_date(item["title"], item["display_date"])
        slug = f"{talk_type_slug(item['talk_type'])}-{compact_date_token(normalized_date)}_{extract_event_slug(item)}.md"
        write_collection_item(
            talks_dir,
            slug,
            {
                "title": item["title"],
                "event": item["event"],
                "location": item["location"],
                "date": normalized_date,
                "display_date": item["display_date"],
                "talk_type": item["talk_type"],
                "presenter_note": item["items"],
                "sequence": item["sequence"],
            },
        )

    for item in teaching:
        normalized_date = normalize_teaching_date(item["display_date"])
        course_id = extract_course_id(item["title"], item["course_url"])
        slug = f"{teaching_type_slug(item['teaching_type'])}-{compact_date_token(normalized_date)}_{course_id}.md"
        write_collection_item(
            teaching_dir,
            slug,
            {
                "title": item["title"],
                "date": normalized_date,
                "display_date": item["display_date"],
                "teaching_type": item["teaching_type"],
                "institution": item["institution"],
                "course_url": item["course_url"],
                "sequence": item["sequence"],
            },
        )


def ensure_plan_file(homepage_root: Path) -> None:
    plan_path = homepage_root / ".tmp" / "260411_update_from_cv.md"
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path.write_text(
        """# Sync Website from LaTeX CV via `_pages/cv.md`

## Summary
- Make `_pages/cv.md` the only CV page on the website and remove the dormant `cv-json` path and its supporting code.
- Use `{resume-main}` as the source of truth, with split ownership:
  - `resume-main/automation/` owns publication parsing from `publication.tex`, `publication.bib`, and `patent.bib`.
  - `homepage-test/scripts/` owns the final site sync into markdown pages and collections.
- Keep the current site structure and public scope: update existing pages only (`/`, `/research/`, `/talks/`, `/teaching/`, `/projects/`, `/cv/`).

## Local Check
1. `python .\\scripts\\sync_from_resume.py --resume-repo ..\\resume-main`
2. `bundle exec jekyll build --config _config.yml,_config_local.yml`
3. `scripts\\serve.bat`
4. Visit `http://localhost:5000/`, `/research/`, `/talks/`, `/teaching/`, `/projects/`, and `/cv/`
""",
        encoding="utf-8",
    )


def resolve_resume_root(homepage_root: Path, explicit_path: str | None) -> Path:
    if explicit_path:
        resume_root = Path(explicit_path).resolve()
        save_local_sync_config(homepage_root, resume_root)
        return resume_root

    local_config = load_local_sync_config(homepage_root)
    config_path = local_config.get("resume_repo")
    if config_path:
        return Path(config_path).resolve()

    env_path = os.environ.get("HOMEPAGE_RESUME_REPO")
    if env_path:
        return Path(env_path).resolve()

    raise SystemExit(
        "Resume repo path not set. Pass --resume-repo, set HOMEPAGE_RESUME_REPO, or create .tmp/sync_from_resume.local.json."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync homepage content from the resume repo.")
    parser.add_argument("--resume-repo", help="Path to resume-main")
    args = parser.parse_args()

    homepage_root = Path(__file__).resolve().parents[1]
    resume_root = resolve_resume_root(homepage_root, args.resume_repo)
    cv_dir = resume_root / "latex" / "cv"

    exported = load_exported_publications(resume_root, homepage_root)
    work = parse_proj_entries(cv_dir / "experience.tex") + parse_proj_entries(cv_dir / "visiting_fellowship.tex")
    skills = parse_skills(cv_dir / "skills.tex")
    interests = parse_research_interests(cv_dir / "research_interest.tex")
    awards = parse_proj_entries(cv_dir / "award.tex")
    activities = parse_activities(cv_dir / "activities.tex")
    projects = parse_projects(cv_dir / "project.tex")
    talks = parse_presentations(cv_dir / "presentation.tex") + parse_presentations(cv_dir / "seminar.tex")
    teaching = parse_teaching(cv_dir / "teaching.tex")

    sync_collections(homepage_root, exported["publications"], exported["patents"], talks, teaching)
    replace_marked_section(homepage_root / "_pages" / "about.md", "about-sections", render_about_block(interests, work, awards, activities))
    replace_marked_section(homepage_root / "_pages" / "projects.md", "projects-sections", render_projects_block(projects))
    replace_marked_section(homepage_root / "_pages" / "cv.md", "cv-sections", render_cv_block(work, skills))
    ensure_plan_file(homepage_root)

    print("Homepage sync complete.")


if __name__ == "__main__":
    main()
