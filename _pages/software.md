---
layout: page
title: software
permalink: /software/
nav: true
nav_order: 7
---

## My R Packages

Below is a list of R packages I’ve developed:

<div class="r-packages">
  {% for package in site.data.r_packages %}
  <div class="r-package">
    <h3>{{ package.name }}</h3>
    <p>{{ package.description }}</p>
    <p>
      Version: {{ package.version }} <br>
      <a href="{{ package.link }}" target="_blank">View on CRAN</a>
    </p>
    <div class="cran-badge">
      <img src="https://cranlogs.r-pkg.org/badges/grand-total/{{ package.name }}" alt="CRAN downloads for {{ package.name }}">
    </div>
  </div>
  <hr>
  {% endfor %}
</div>