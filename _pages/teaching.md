---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: false
---
(G: Graduate, U: Undergraduate)

{% assign taught_courses = site.teaching | where: "teaching_type", "lecturer" | sort: "sequence" | reverse %}
{% assign assistant_courses = site.teaching | where: "teaching_type", "assistant" | sort: "sequence" | reverse %}

## Courses Taught

### @ POSTECH

<ul>
{% for item in taught_courses %}
  <li>
    {% if item.course_url %}<a href="{{ item.course_url }}"><strong>{{ item.title }}</strong></a>{% else %}<strong>{{ item.title }}</strong>{% endif %}
  </li>
{% endfor %}
</ul>

## Teaching Assistant @ POSTECH

<ul>
{% for item in assistant_courses %}
  <li><strong>{{ item.title }}</strong></li>
{% endfor %}
</ul>
