---
layout: default
title: "Short Bio — Asterios Katsifodimos"
---

##### Short Bio

Asterios Katsifodimos is an Assistant Professor at [TU Delft](https://www.tudelft.nl/) and an Amazon Scholar at [AWS](https://www.amazon.science/research-areas/information-and-knowledge-management), where he leads the [Data-intensive Systems Group](https://dis.ewi.tudelft.nl). His research focuses on cloud application runtimes, stream processing, and data discovery. His work has found applications in real-world systems including Apache Flink and systems within Amazon's Cloud.

Katsifodimos received his PhD from [INRIA Saclay](https://www.inria.fr/saclay/) and [Université Paris-Sud](https://www.universite-paris-saclay.fr) in 2013, supervised by [Ioana Manolescu](http://www-rocq.inria.fr/~manolesc/). Before joining TU Delft in 2017, he held positions at the [SAP Innovation Center](https://icn.sap.com) and [TU Berlin](https://www.dima.tu-berlin.de/), working with [Volker Markl](https://www.dima.tu-berlin.de/menue/staff/volker_markl/). He completed his BSc and MSc at the University of Cyprus, working with [Marios Dikaiakos](http://www.cs.ucy.ac.cy/~mdd/).

He is the recipient of the ACM SIGMOD Systems Award (2023), an NWO VIDI Grant (2022), the ACM DEBS Best Paper Award (2021), the EDBT Best Paper Award (2019), the EDBT Best Demo Award (2023), and the ACM SIGMOD Research Highlights Award (2015).



##### Career Timeline

<div class="timeline">
{% for item in site.data.timeline %}
  <div class="timeline-item">
    <div class="timeline-year">{{ item.year }}</div>
    <div class="timeline-dot{% if item.current %} current{% endif %}"></div>
    <div class="timeline-body">
      <span class="{{ item.icon }} timeline-icon"></span>
      <strong>{{ item.title }}</strong> &mdash; {{ item.org }}
      {% if item.detail %}<div class="timeline-detail">{{ item.detail }}</div>{% endif %}
    </div>
  </div>
{% endfor %}
</div>
