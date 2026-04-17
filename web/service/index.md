---
layout: default
title: "Asterios Katsifodimos | Assistant Professor, TU Delft"
---

<h5>Scientific Community Service</h5>

<div id="service" class="row">
<div class="col-sm-12">



<h6>Chair / Organizer</h6>

<table class="teaching-table">
  <thead><tr><th>Venue</th><th>Role</th></tr></thead>
  <tbody>
    {% for entry in site.data.service.chairs %}
    <tr><td>{{ entry.venue }}</td><td>{{ entry.role }}</td></tr>
    {% endfor %}
  </tbody>
</table>

<br>

<h6>Program Committees</h6>

<table class="teaching-table">
  <thead><tr><th>Venue</th><th>Years</th></tr></thead>
  <tbody>
    {% for entry in site.data.service.pc_member %}
    <tr><td>{% if entry.link %}<a href="{{ entry.link }}">{{ entry.venue }}</a>{% else %}{{ entry.venue }}{% endif %}</td><td>{{ entry.years }}</td></tr>
    {% endfor %}
  </tbody>
</table>

</div>
</div>
