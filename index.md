---
layout: default
title: "Asterios Katsifodimos | Asst. Professor, TU Delft"
---

<!-- Hero -->
<div id="top" class="row align-items-start">
<div class="col-sm-8">

<p class="lead lead-xl"><strong>
Asst. Professor at <a href="http://www.tudelft.nl/">TU Delft</a> and Amazon Scholar (<a href="https://www.amazon.science/research-areas/information-and-knowledge-management">AWS</a>).</strong>
</p>

<p>I lead the <a href="https://dis.ewi.tudelft.nl">Data-intensive Systems Group</a> at TU Delft. I work in the broad area of data systems research; most of my research at the moment focuses on Cloud application runtimes, and data discovery. Over the years, my research has found applications in multiple real-world systems, including Apache Flink, and systems within Amazon's Cloud. Before joining TU Delft in 2017, I held positions at the <a href="https://icn.sap.com">SAP Innovation Center</a>, as well as at <a href="http://www.dima.tu-berlin.de/menue/database_systems_and_information_management_group/?no_cache=1">TU Berlin</a>, working with <a href="https://www.dima.tu-berlin.de/menue/staff/volker_markl/">Volker Markl</a>. I received my PhD from <a href="http://www.inria.fr/saclay/">INRIA Saclay</a>/<a href="https://www.universite-paris-saclay.fr">Université Paris-Sud 11</a> in 2013, supervised by <a href="http://www-rocq.inria.fr/~manolesc/">Ioana Manolescu</a>. I completed my BSc and MSc at the University of Cyprus, working with <a href="http://www.cs.ucy.ac.cy/~mdd/">Marios Dikaiakos</a>.

</p>

<p><a href="/bio/"><span class="fa-solid fa-id-card"></span> Short bio &amp; timeline</a></p>

<div class="awards-row">
<strong><span class="fa-solid fa-trophy"></span> Awards</strong><br>
<div class="awards-content">
{% for a in site.data.awards %}<span class="badge-{{ a.type }}"><span class="fa-solid fa-{% if a.type == 'grant' %}flask{% else %}award{% endif %} badge-icon"></span>{{ a.name }}</span>
{% endfor %}</div>
</div>

</div>
<div class="col-md-4">
<div class="profile-card">
  <img src="assets/asterios.katsifodimos-2022.jpg" class="profile-photo" alt="Asterios Katsifodimos - Αστέριος Κατσιφοδήμος">
  <div class="profile-divider"></div>
  <div class="profile-contact">
    <div class="profile-contact-item">
      <span class="fa-solid fa-envelope profile-contact-icon"></span>
      <a href="mailto:A.Katsifodimos@tudelft.nl">A.Katsifodimos@tudelft.nl</a>
    </div>
    <div class="profile-contact-item">
      <span class="fa-solid fa-map-marker-alt profile-contact-icon"></span>
      <span>Room 1E100, Van Mourik Broekmanweg 6<br>2628XE Delft, Netherlands</span>
    </div>
  </div>
  <div class="profile-divider"></div>
  <div class="profile-socials">
    <a href="https://scholar.google.com/citations?user=1KdkcSoAAAAJ&hl=en&oi=ao"><span class="fa-solid fa-graduation-cap"></span> Scholar</a>
    <a href="https://www.linkedin.com/in/asteriosk/"><span class="fa-brands fa-linkedin"></span> LinkedIn</a>
    <a href="https://github.com/asteriosk"><span class="fa-brands fa-github"></span> GitHub</a>
    <a href="https://x.com/kAsterios"><span class="fa-brands fa-x-twitter"></span> X</a>
  </div>
</div>
</div>
</div>


<!-- Research Areas -->
<div id="research" class="row" style="padding-top: 1rem;">
<div class="col-12"><h5>Research Areas</h5></div>

<div class="col-md-4 mb-3">
<div class="research-card">
  <div class="card-icon"><span class="fa-solid fa-cloud"></span></div>
  <h6>Cloud Runtimes</h6>
  <p style="font-size:0.9rem; margin-bottom:0.75rem;">Building programming models and runtimes that bring ACID transactions to stateful serverless in the Cloud.</p>
</div>
</div>

<div class="col-md-4 mb-3">
<div class="research-card">
  <div class="card-icon"><span class="fa-solid fa-water"></span></div>
  <h6>Stream Processing</h6>
  <p style="font-size:0.9rem; margin-bottom:0.75rem;">Designing fault-tolerant, high-throughput streaming systems that scale to billions of events per second.</p>
</div>
</div>

<div class="col-md-4 mb-3">
<div class="research-card">
  <div class="card-icon"><span class="fa-solid fa-database"></span></div>
  <h6>Data Discovery</h6>
  <p style="font-size:0.9rem; margin-bottom:0.75rem;">Automating the discovery of datasets and their relationships in data lakes and enterprise repositories.</p>
</div>
</div>
</div>

