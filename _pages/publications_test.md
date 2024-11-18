---
layout: page
title: "Test Keywords"
permalink: /publications_test/
---



# Scholar Test

<pre>
{% for entry in site.scholar.entries %}
  {{ entry | jsonify }}
{% endfor %}
</pre>
