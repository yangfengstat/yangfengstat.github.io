---
layout: page
permalink: /posts/
title: blog
description: my random thoughts on random stuff.
nav: true
nav_order: 9
---


{% for post in site.posts %}
- **{{ post.date | date: "%Y-%m-%d" }}** [{{ post.title }}]({{ post.url }})
{% endfor %}
