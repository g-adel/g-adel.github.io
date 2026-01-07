---
title: Generative Art
permalink: /generative/
secondary_content: |
  ## About
  
  A collection of algorithmic art exploring patterns, emergence, and computational aesthetics.
  
  Each project represents a different exploration of generative systems.
---

# Generative Art Gallery

Click on any project to explore the full collection.

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">

{% for project in site.generative %}
  {% comment %}Get the first media file from this project's folder{% endcomment %}
  {% assign project_path = project.path | split: "/" | slice: 0, 2 | join: "/" %}
  {% assign project_files = site.static_files | where_exp: "file", "file.path contains project_path" %}
  {% assign media_files = project_files | where_exp: "file", "file.extname == '.png' or file.extname == '.jpg' or file.extname == '.gif' or file.extname == '.mp4'" | sort: "name" %}
  {% assign first_file = media_files | first %}
  {% assign file_count = media_files | size %}
  
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 4px; transition: box-shadow 0.2s;">
    <h3 style="margin-top: 0;">
      <a href="{{ project.url }}" style="text-decoration: none; color: #333;">
        {{ project.title }}
      </a>
    </h3>
    <a href="{{ project.url }}" style="display: block;">
      {% if first_file %}
        {% assign file_ext = first_file.extname | remove: '.' %}
        {% if file_ext == 'mp4' or file_ext == 'webm' %}
          <video style="width: 100%; height: auto;" muted loop onmouseover="this.play()" onmouseout="this.pause()">
            <source src="{{ first_file.path }}" type="video/{{ file_ext }}">
          </video>
        {% else %}
          <img src="{{ first_file.path }}" alt="{{ project.title }}" style="width: 100%; height: auto;">
        {% endif %}
      {% endif %}
    </a>
    <p style="font-size: 0.9rem; color: #666; margin-bottom: 0.5rem;">
      {{ file_count }} {% if file_count == 1 %}piece{% else %}pieces{% endif %}
    </p>
    <p style="font-size: 0.85rem; color: #888; margin: 0;">{{ project.description }}</p>
  </div>
{% endfor %}

</div>
