---
layout: generative-project
title: "Trails"
permalink: /generative/trails/
project_name: Trails
project_files:
  - Trails_1.png
  - Trails_2.png
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "Trails" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# Trails

Capturing motion and pathways through generative processes.
