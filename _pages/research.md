---
layout: archive
title: "Research"
permalink: /research/
author_profile: false
---

<!-- {% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %} -->

{% assign journals = site.publications | where: "pub_type", "journal" | sort: "date" | reverse %}
{% assign conferences = site.publications | where: "pub_type", "conference" | sort: "date" | reverse %}
{% assign working_papers = site.publications | where: "pub_type", "working_paper" | sort: "date" | reverse %}
{% assign patents = site.publications | where: "pub_type", "patent" | sort: "date" | reverse %}

## Journal Articles

<ol>
{% for post in journals %}
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
{% for post in conferences %}
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
{% for post in working_papers %}
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
{% for post in patents %}
  <li>{{ post.citation }}</li>
{% endfor %}
</ol>
