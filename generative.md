---
title: Generative Art
permalink: /generative/
secondary_content: |

---

# Generative Art

<div class="generative-grid">

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

  <div class="generative-item">
     <h3>
      <a href="{{ project.url }}">
        {{ project.title }}
      </a>
        </h3>
        <a href="{{ project.url }}" class="generative-item-link">
      {% if first_file %}
        {% assign file_ext = first_file.path | split: '.' | last | downcase %}
        {% assign file_url = first_file.path | relative_url | replace: '/_generative/', '/generative/' %}
        {% if file_ext == 'mp4' or file_ext == 'webm' %}
        <video src="{{ file_url }}" muted loop playsinline onmouseover="this.play()" onmouseout="this.pause()">
        </video>
        {% else %}
        <img src="{{ file_url }}" alt="{{ project.title }}">
        {% endif %}
      {% else %}
        <div class="no-preview-placeholder">
          <span>No Preview</span>
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
