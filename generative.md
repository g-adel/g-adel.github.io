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

{% for project in site.data.generative_projects %}
  <div style="border: 1px solid #ddd; padding: 1rem; border-radius: 4px; transition: box-shadow 0.2s;">
    <h3 style="margin-top: 0;">
      <a href="/generative/{{ project.name | downcase }}/" style="text-decoration: none; color: #333;">
        {{ project.name }}
      </a>
    </h3>
    <a href="/generative/{{ project.name | downcase }}/" style="display: block;">
      {% assign first_file = project.files[0] %}
      {% assign file_ext = first_file | split: '.' | last %}
      {% if file_ext == 'mp4' or file_ext == 'webm' %}
        <video style="width: 100%; height: auto;" muted loop onmouseover="this.play()" onmouseout="this.pause()">
          <source src="/Generative/{{ first_file }}" type="video/{{ file_ext }}">
        </video>
      {% else %}
        <img src="/Generative/{{ first_file }}" alt="{{ project.name }}" style="width: 100%; height: auto;">
      {% endif %}
    </a>
    <p style="font-size: 0.9rem; color: #666; margin-bottom: 0;">
      {{ project.files | size }} {% if project.files.size == 1 %}piece{% else %}pieces{% endif %}
    </p>
  </div>
{% endfor %}

</div>
