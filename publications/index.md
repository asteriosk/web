---
layout: default
title: "Asterios Katsifodimos | Assistant Professor, TU Delft"
---
<div id="publications" class="row" style="padding-top: 1rem;">
<div style="text-align: justify;" class="col-sm-12">
<h5>Selected Papers</h5>

<div class="pub-cards-grid">
{% for sp in site.data.selected_publications %}
  {% assign pub = site.data.publications | where: "id", sp.id | first %}
  {% assign merged = pub | default: sp %}
  {% if sp.award %}{% assign award = sp.award %}{% else %}{% assign award = pub.award %}{% endif %}
  {% include pub-highlight.html publication=merged award=award desc=sp.desc %}
{% endfor %}
</div>

<h5>Publications</h5>
<i>For a complete list, check my <a href="https://dblp.org/pid/64/7497.html">DBLP entry</a></i>
<br/>
<br/>
{% assign pubs_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}
{% for year_group in pubs_by_year %}
<h6 style="margin-top:1.2rem;"><strong>{{ year_group.name }}</strong></h6>
<div class="pub-highlights">
{% for pub in year_group.items %}
  <div class="pub-highlight-card">
    <div class="pub-highlight-venue-col">
      <span class="pub-highlight-venue">{{ pub.label }}</span>
      <div class="pub-highlight-links">
        {% if pub.pdf %}{% if pub.pdf contains "http" %}<a href="{{ pub.pdf }}"><span class="fa fa-file-pdf"></span> PDF</a>{% else %}<a href="{{ site.url}}/{{ pub.pdf }}"><span class="fa fa-file-pdf"></span> PDF</a>{% endif %}{% endif %}
        {% if pub.link %}<a href="{{ pub.link }}"><span class="fa fa-up-right-from-square"></span> Link</a>{% endif %}
        {% if pub.poster %}<a href="{{ site.url}}/{{ pub.poster }}"><span class="fa fa-file-pdf"></span> Poster</a>{% endif %}
        {% if pub.slides %}<a href="{{ site.url}}/{{ pub.slides }}"><span class="fa fa-file-pdf"></span> Slides</a>{% endif %}
      </div>
    </div>
    <div class="pub-highlight-main">
      <div class="pub-highlight-title">{{ pub.title }}</div>
      <div class="pub-highlight-authors">{{ pub.authors }}</div>
      <div class="pub-highlight-venue-text">{{ pub.venue }}</div>
    </div>
  </div>
{% endfor %}
</div>
{% endfor %}

</div>
</div>
