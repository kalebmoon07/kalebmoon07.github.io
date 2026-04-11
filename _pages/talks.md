---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: false
---

(*: attended as the presenter)

{% assign intl_talks = site.talks | where: "talk_type", "conference_international" | sort: "sequence" | reverse %}
{% assign domestic_talks = site.talks | where: "talk_type", "conference_domestic" | sort: "sequence" | reverse %}
{% assign seminar_talks = site.talks | where: "talk_type", "seminar" | sort: "sequence" | reverse %}

## Conference Presentations (International)

<ul>
{% for talk in intl_talks %}
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
{% for talk in domestic_talks %}
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
{% for talk in seminar_talks %}
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
