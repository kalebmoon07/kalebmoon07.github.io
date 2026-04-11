---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Industrial and Management Engineering, POSTECH (Pohang University of Science and Technology), 2020-2025
  * Thesis: Multilevel Optimization for Precision Medicine: A Boolean Network Control Approach
  * Advisor: Prof. [Kangbok Lee](https://www.msolab.org/)
* M.S. in Industrial and Management Engineering, POSTECH (Pohang University of Science and Technology), 2018-2020
  * Thesis: Strategic Location Problem for Last-mile Delivery with Relaying Drones
  * Advisor: Prof. [Kangbok Lee](https://www.msolab.org/)
* B.S. in Industrial and Management Engineering, POSTECH (Pohang University of Science and Technology), 2015-2018

<!-- BEGIN AUTO-SYNC: cv-sections -->
Work experience
======
* **Postdoctoral Researcher**, Department of Industrial and Management Engineering ; POSTECH (Pohang University of Science and Technology), Pohang, Korea (Aug 2025 – present)
  * Advisor: Prof. Kangbok Lee

* **Lecturer**, Department of Industrial and Management Engineering ; POSTECH (Pohang University of Science and Technology), Pohang, Korea (Aug 2025 – present)

* **Visiting Research Fellow**, Department of Industrial Engineering ; Swanson School of Engineering at University of Pittsburgh, Pittsburgh, PA, USA (Dec 2025 – Jan 2026)
  * Host: Prof. Bo Zeng

* **Visiting Predoctoral Fellow**, Modèles & Technologies pour la Vérification Team ; Laboratoire Bordelais de Recherche en Informatique (LaBRI) at U. of Bordeaux, Talence, France (Jun & Nov 2024, Sep 2025)
  * Host: Dr. Loïc Paulevé

* **Visiting Predoctoral Fellow**, Department of Technology, Operations, and Statistics ; Stern School of Business, New York University, New York, NY, USA (Jan 2024)
  * Host: Prof. Michael L. Pinedo

* **Visiting Predoctoral Fellow**, Operations Department ; Kellogg School of Management, Northwestern University, Evanston, IL, USA (Jul – Aug 2017)
  * Host: Prof. Sunil Chopra

* **Internship**, Administration Headquarters, PMGROW Corp., Uiwang, Korea (Jul – Aug 2016)

Skills
======
* Language: English (fluent), Korean (native)
* Programming: Python, Java, C, C++, R, SQL, MariaDB, Qt
* Optimization tools: Gurobi, CPLEX, Google OR-Tools, Pyomo, CVX, SCIP, CP Optimizer, Fujitsu DA
* DevOps: Git, GitHub, Docker
* OA & RPA: MS 365, LaTeX, Beamer, TikZ, Markdown, MS Power Automate, Graphviz
<!-- END AUTO-SYNC: cv-sections -->

Publications
======
{% assign cv_journals = site.publications | where: "pub_type", "journal" | sort: "date" | reverse %}
{% assign cv_conferences = site.publications | where: "pub_type", "conference" | sort: "date" | reverse %}
{% assign cv_working = site.publications | where: "pub_type", "working_paper" | sort: "date" | reverse %}
{% assign cv_patents = site.publications | where: "pub_type", "patent" | sort: "date" | reverse %}

## Journal Articles
<ol>
{% for post in cv_journals %}
  <li>
    {{ post.citation }}
    {% if post.doi and post.doi != "" %}<a href="{{ post.paperurl }}">doi: {{ post.doi }}</a>{% endif %}
    {% if post.notes and post.notes.size > 0 %}
    <ul>
      {% for note in post.notes %}
      <li>{{ note }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ol>

## Conference Proceedings
<ol>
{% for post in cv_conferences %}
  <li>
    {{ post.citation }}
    {% if post.doi and post.doi != "" %}<a href="{{ post.paperurl }}">doi: {{ post.doi }}</a>{% endif %}
    {% if post.notes and post.notes.size > 0 %}
    <ul>
      {% for note in post.notes %}
      <li>{{ note }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ol>

## Working Papers
<ol>
{% for post in cv_working %}
  <li>
    {{ post.citation }}
    {% if post.doi and post.doi != "" %}<a href="{{ post.paperurl }}">doi: {{ post.doi }}</a>{% endif %}
    {% if post.notes and post.notes.size > 0 %}
    <ul>
      {% for note in post.notes %}
      <li>{{ note }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ol>

## Patents
<ol>
{% for post in cv_patents %}
  <li>{{ post.citation }}</li>
{% endfor %}
</ol>

Talks
======
{% assign cv_intl_talks = site.talks | where: "talk_type", "conference_international" | sort: "sequence" | reverse %}
{% assign cv_domestic_talks = site.talks | where: "talk_type", "conference_domestic" | sort: "sequence" | reverse %}
{% assign cv_seminar_talks = site.talks | where: "talk_type", "seminar" | sort: "sequence" | reverse %}

## Conference Presentations (International)
<ul>
{% for talk in cv_intl_talks %}
  <li>
    <strong>{{ talk.title }}</strong>, {{ talk.location }} ({{ talk.display_date }})
    <br /><em>{{ talk.event }}</em>
    {% if talk.presenter_note and talk.presenter_note.size > 0 %}
    <ul>
      {% for note in talk.presenter_note %}
      <li>{{ note }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ul>

## Conference Presentations (Domestic)
<ul>
{% for talk in cv_domestic_talks %}
  <li>
    <strong>{{ talk.title }}</strong>, {{ talk.location }} ({{ talk.display_date }})
    <br /><em>{{ talk.event }}</em>
    {% if talk.presenter_note and talk.presenter_note.size > 0 %}
    <ul>
      {% for note in talk.presenter_note %}
      <li>{{ note }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ul>

## Seminar & Research Talks
<ul>
{% for talk in cv_seminar_talks %}
  <li>
    <strong>{{ talk.title }}</strong>, {{ talk.location }} ({{ talk.display_date }})
    <br /><em>{{ talk.event }}</em>
    {% if talk.presenter_note and talk.presenter_note.size > 0 %}
    <ul>
      {% for note in talk.presenter_note %}
      <li>{{ note }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
{% endfor %}
</ul>

Teaching
======
{% assign cv_lecturer = site.teaching | where: "teaching_type", "lecturer" | sort: "sequence" | reverse %}
{% assign cv_assistant = site.teaching | where: "teaching_type", "assistant" | sort: "sequence" | reverse %}

## Lecturer
<ul>
{% for item in cv_lecturer %}
  <li>
    {% if item.course_url %}<a href="{{ item.course_url }}"><strong>{{ item.title }}</strong></a>{% else %}<strong>{{ item.title }}</strong>{% endif %}
  </li>
{% endfor %}
</ul>

## Teaching Assistant
<ul>
{% for item in cv_assistant %}
  <li>
    <strong>{{ item.title }}</strong>
  </li>
{% endfor %}
</ul>
