---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

## Pages

- [About]({{ '/' | relative_url }})
- [Publications]({{ '/publications/' | relative_url }})
- [Curriculum Vitae]({{ '/cv/' | relative_url }})

## Papers

{% for paper in site.publications reversed %}
- [{{ paper.title }}]({{ paper.url | relative_url }})
{% endfor %}
