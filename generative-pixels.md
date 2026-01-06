---
layout: generative-project
title: "Pixels"
permalink: /generative/pixels/
project_name: Pixels
project_files:
  - Pixels_1.gif
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "Pixels" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# Pixels

An animated exploration of pixel-based generative art.
