---
layout: default
title: "Asterios Katsifodimos | Assistant Professor, TU Delft"
---

<h5>People</h5>

<div id="people" class="row">


<div class="col-12 mb-1">
<p class="people-section-label"><span class="fa-solid fa-user-graduate" style="margin-right:6px;"></span>PhD Students</p>
<div class="people-list">
{% for student in site.data.supervision.phd_students %}
{% include student-card.html student=student %}
{% endfor %}
</div>
</div>

<div class="col-12 mb-1">
<p class="people-section-label"><span class="fa-solid fa-microscope" style="margin-right:6px;"></span>Postdocs</p>
<div class="people-list">
{% for student in site.data.supervision.postdocs %}
{% include student-card.html student=student %}
{% endfor %}
</div>
</div>

<div class="col-12 mb-1">
<p class="people-section-label"><span class="fa-solid fa-graduation-cap" style="margin-right:6px;"></span>Master Students</p>
<div class="people-list">
{% for student in site.data.supervision.masters %}
{% include student-card.html student=student %}
{% endfor %}
</div>
</div>

</div>
