---
layout: default
title: "Asterios Katsifodimos | Assistant Professor, TU Delft"
---


##### University Courses

<br>

{% for institution in site.data.teaching %}
<h5>{{ institution.institution }}</h5>
<table class="teaching-table">
  <thead>
    <tr>
      <th>Course</th>
      <th>Period</th>
      <th>Years</th>
      <th>Level</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    {% for course in institution.courses %}
    <tr>
      <td>{% if course.link %}<a href="{{ course.link }}">{{ course.name }}</a>{% else %}{{ course.name }}{% endif %}</td>
      <td>{{ course.period }}</td>
      <td>{% if course.end_year == course.start_year %}{{ course.start_year }}{% elsif course.end_year %}{{ course.start_year }}–{{ course.end_year }}{% else %}{{ course.start_year }}–present{% endif %}</td>
      <td>{% if course.level == "MSc" %}<span class="fa-solid fa-user-graduate"></span>{% elsif course.level == "BSc" %}<span class="fa-solid fa-graduation-cap"></span>{% elsif course.level == "ProfEd" %}<span class="fa-solid fa-briefcase"></span>{% endif %} {{ course.level }}</td>
      <td>{{ course.description }}{% if course.collaborator_name %} · with <a href="{{ course.collaborator_link }}">{{ course.collaborator_name }}</a>{% endif %}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
<br/>
{% endfor %}
