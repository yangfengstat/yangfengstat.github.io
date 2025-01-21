---
layout: conference-default
title: "Speakers"
---

# Invited Speakers (Confirmed)

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; background-color: #f9f9f9; padding: 2rem; border-radius: 8px;">
  {% for speaker in site.data.speakers %}
  <div style="background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 1rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; transition: transform 0.2s ease, box-shadow 0.2s ease;">
    <h3 style="font-size: 1.25rem; font-weight: bold; color: #333; margin-bottom: 0.5rem;">{{ speaker.name }}</h3>
    <p style="font-size: 1rem; color: #666;">{{ speaker.affiliation }}</p>
  </div>
  {% endfor %}
</div>