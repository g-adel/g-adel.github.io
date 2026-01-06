---
layout: generative-project
title: "Transformations"
permalink: /generative/transformations/
project_name: Transformations
project_files:
  - Transformations_1.mp4
  - Transformations_1.png
  - Transformations_2.png
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "Transformations" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# Transformations

Exploring metamorphosis and change through algorithmic art.
