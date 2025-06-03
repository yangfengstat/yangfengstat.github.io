---
layout: conference-default
title: "SNAB 2025"
nav_title: SNAB 2025
permalink: /snab2025/
---
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

  :root {
    --accent-color: #3b82f6;
    --card-bg: #ffffff;
    --card-hover-bg: #f3f7fb;
  }

  body {
    font-family: 'Inter', sans-serif;
    background: #f0f4f8;
    color: #333;
    padding: 1rem;
  }

  h1, h2 {
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--accent-color);
    text-align: center;
    margin: 2rem 0 1rem;
  }

  .section {
    max-width: 1200px;
    margin: 0 auto 2rem;
    padding: 0 1rem;
  }

  .organizer-list {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.5rem;
    padding: 0;
    margin: 2rem 0;
  }

  .organizer-list li {
    background: var(--card-bg);
    border-left: 4px solid var(--accent-color);
    border-radius: 16px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
    display: flex;
    align-items: center;
    padding: 1.25rem;
  }

  .organizer-list li:hover {
    background: var(--card-hover-bg);
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
  }

  .profile-photo {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid var(--accent-color);
    margin-right: 1.5rem;
    flex-shrink: 0;
  }

  .organizer-info h3 {
    margin: 0 0 0.25rem;
    font-weight: 600;
    font-size: 1.2rem;
  }

  .organizer-info p {
    margin: 0;
    font-size: 1rem;
    color: #666;
  }
</style>

<div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin: 2rem 0 1rem;">
  <img src="assets/img/snab.jpg" alt="SNAB 2025 Logo" style="max-height: 90px; opacity: 1; border-radius: 6px;">
  <h1 style="margin: 0; font-size: 2.2rem; text-transform: uppercase; letter-spacing: 1px; color: var(--accent-color);">Welcome to SNAB 2025</h1>
</div>

The **2025 Workshop on Statistical Network Analysis and Beyond (SNAB 2025)** will take place on **June 2-4, 2025** at the renowned [Hotel New Otani](https://www.newotani.co.jp/en/tokyo/) in **Tokyo, Japan**.

![Hotel New Otani](assets/img/hotel.jpg "Hotel New Otani, Tokyo"){: style="border-radius: 10px; max-width: 100%; margin: auto; display: block;" }

---

## About the Conference

SNAB 2025 is a **three-day workshop** bringing together experts in **network science** and related fields. The conference serves as a platform for sharing cutting-edge research and fostering collaboration.

### Topics Include:
- Statistical network modeling 
- Tensor analysis and modeling
- Deep learning
- Transfer learning and multi-task learning
- Text analysis in network structures
- Applications in social, biological, and public health

---

## Organizers

<section class="section">
  <ul class="organizer-list">
    {% assign organizers = "Yang Feng|New York University|Yang_Feng.jpg,Jiashun Jin|Carnegie Mellon University|Jiashun_Jin.jpg,Qingfeng Liu|Hosei University|Qingfeng_Liu.jpg,Maggie Niu|Penn State University|Maggie_Niu.jpg,Ji Zhu|University of Michigan|Ji_Zhu.jpg" | split: "," %}
    {% for org in organizers %}
      {% assign parts = org | split: "|" %}
      <li>
        <img src="{{ '/assets/images/speakers/' | append: parts[2] | relative_url }}" alt="{{ parts[0] }}" class="profile-photo">
        <div class="organizer-info">
          <h3><a href="{% case parts[0] %}{% when "Yang Feng" %}https://yangfengstat.github.io/{% when "Jiashun Jin" %}https://www.stat.cmu.edu/~jiashun/{% when "Qingfeng Liu" %}https://qingfeng-liu.github.io/index1.html{% when "Maggie Niu" %}https://sites.google.com/view/maggiexniu/{% when "Ji Zhu" %}https://dept.stat.lsa.umich.edu/~jizhu/{% endcase %}">{{ parts[0] }}</a></h3>
          <p>{{ parts[1] }}</p>
        </div>
      </li>
    {% endfor %}
  </ul>
</section>

---

## Past SNAB Workshops

- [**SNAB 2024**](https://sites.google.com/view/snab2024/) - Bahamas  
- [**SNAB 2023**](https://www.snab2023.org/) - Anchorage, Alaska  
- [**SNAB 2022**](assets/pdf/SNAB2022 Workshop Brochure.pdf) - New York  
- [**SNAB 2021**](https://dept.stat.lsa.umich.edu/~jizhu/snab2021/) - Virtual  

---

## Sponsors

We are grateful to our sponsors for their support of SNAB 2025:

![IMS](assets/img/ims.png "IMS"){: style="border-radius: 10px; max-width: 20%; margin: 20px auto; display: block;" }

---

We look forward to seeing you at **SNAB 2025** in Tokyo!
