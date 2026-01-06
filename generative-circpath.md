---
layout: generative-project
title: "CircPath"
permalink: /generative/circpath/
project_name: CircPath
project_files:
  - CircPath_1.png
secondary_content: |
  ## Other Projects
  
  {% for project in site.data.generative_projects %}
  {% if project.name != "CircPath" %}
  - [{{ project.name }}](/generative/{{ project.name | downcase }}/)
  {% endif %}
  {% endfor %}
---

# CircPath

A generative art project exploring circular paths and patterns.
