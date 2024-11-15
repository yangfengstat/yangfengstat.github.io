---
layout: page
title: software
permalink: /software/
nav: true
nav_order: 7
---
<style>
/* Custom styles for the software page */
.r-packages {
  margin-top: 20px;
}

.r-package {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.r-package h3 {
  margin-bottom: 5px;
  font-size: 1.5em;
}

.r-package p {
  margin: 5px 0;
  font-size: 0.9em;
}

.r-package a {
  color: #0056b3;
  text-decoration: none;
}

.r-package a:hover {
  text-decoration: underline;
}
</style>

## My R Packages

Below is a list of R packages I’ve developed:

<div class="r-packages">
  {% for package in site.data.r_packages %}
  <div class="r-package">
    <h3>{{ package.name }}</h3>
    <p>{{ package.description }}</p>
    <p>
      <strong>Version:</strong> {{ package.version }} <br>
  
      <a href="{{ package.link }}" target="_blank">View on CRAN</a> 
    </p>
  </div>
  <hr>
  {% endfor %}
</div>