---
title: Generative Art
permalink: /generative/
secondary_content: |

---

# Generative Art

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 2rem; margin-top: 2rem;">

{% assign generative_collection = site.collections | where: "label", "generative" | first %}
{% for project in site.generative %}
  {% assign project_dir = project.path | remove: 'index.md' %}
  {% assign first_file = nil %}
  
  {% for file in generative_collection.files %}
    {% if file.path contains project_dir %}
        {% assign ext = file.path | split: '.' | last | downcase %}
        {% if "jpg jpeg png gif mp4 webm" contains ext %}
            {% assign first_file = file %}
            {% break %}
        {% endif %}
    {% endif %}
  {% endfor %}

  <div style="padding: 0rem; border-radius: 4px; transition: box-shadow 0.2s;">
     <h3 style="margin-top: 0; text-align: center;">
      <a href="{{ project.url }}" style="text-decoration: none; color: #333;">
        {{ project.title }}
      </a>
        </h3>
        <a href="{{ project.url }}" style="display: block; text-align: center;">
      {% if first_file %}
        {% assign file_ext = first_file.path | split: '.' | last | downcase %}
        {% assign file_url = first_file.path | relative_url | replace: '/_generative/', '/generative/' %}
        {% if file_ext == 'mp4' or file_ext == 'webm' %}
        <video src="{{ file_url }}" style="width: 100%; height: auto;" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()">
        </video>
        {% else %}
        <img src="{{ file_url }}" alt="{{ project.title }}" style="width: 100%; height: auto;">
        {% endif %}
      {% else %}
        <div style="width: 100%; height: 200px; background: #eee; display: flex; align-items: center; justify-content: center;">
        No Preview
        </div>
      {% endif %}
        </a>
        
        <!-- {% assign file_count = 0 %}
        {% for file in generative_collection.files %}
        {% if file.path contains project_dir %}
         {% assign ext = file.path | split: '.' | last | downcase %}
         {% if "jpg jpeg png gif mp4 webm" contains ext %}
            {% assign file_count = file_count | plus: 1 %}
         {% endif %}
        {% endif %}
        {% endfor %} -->

        <!-- <p style="font-size: 0.9rem; color: #666; margin-bottom: 0;">
      {{ file_count }} {% if file_count == 1 %}piece{% else %}pieces{% endif %}
        </p> -->
  </div>
{% endfor %}

</div>
