---
layout: generative-project
title: "Salt"
permalink: /generative/salt/
project_name: Salt
project_files:
  - Salt_1.png
  - Salt_2.mp4
  - Salt_3.png
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "Salt" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# Salt

Exploring crystalline patterns and salt-like structures through code.
