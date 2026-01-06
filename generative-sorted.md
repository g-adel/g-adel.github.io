---
layout: generative-project
title: "Sorted"
permalink: /generative/sorted/
project_name: Sorted
project_files:
  - Sorted_1.png
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "Sorted" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# Sorted

Visualizing sorting algorithms and ordered structures.
