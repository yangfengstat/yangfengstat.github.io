---
layout: page
title: News
permalink: /news/
nav_order: 4
---

# News

{% for post in site.news %}
- **{{ post.date | date: "%Y-%m-%d" }}** [{{ post.title }}]({{ post.url }})
{% endfor %}