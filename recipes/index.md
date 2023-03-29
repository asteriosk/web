---
layout: default
title: "Asterios Katsifodimos | Assistant Professor, TU Delft"
recipes:
 - {title: Meatballs with Red Sauce, url: meatballs-red-sauce.html}
---
<div id="recipes" class="row">
<div style="text-align: justify;" class="col-sm-12">
<h5>Recipes</h5>
<br/>

{% for rcp in page.recipes %}
<!-- {% if rcp('section')? %}
<h6><strong>{{rcp.title}}</strong></h6>
{% else %}
 -->&nbsp;
<dl class="row">
  <dd class="col-sm-9">
    <a href="{{ site.url}}/recipes/{{ rcp.url }}"><strong>{{ rcp.title }}</strong></a>
  </dd>
</dl>
{% endif %}
{% endfor %}

</div>
