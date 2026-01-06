---
layout: generative-project
title: "Sand"
permalink: /generative/sand/
project_name: Sand
project_files:
  - Sand_1.png
  - Sand_2.mp4
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "Sand" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# Sand

Simulating the flow and patterns of sand particles.
