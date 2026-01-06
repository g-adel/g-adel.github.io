# Golden Layout Usage Guide

The `golden` layout is now the default layout for all pages on this site. It features a beautiful golden ratio-based design with multiple customizable regions.

## Layout Structure

The layout has 5 distinct regions you can customize:

### 1. **Main Content (Right Square)** - Primary Area
- This is where your page's main content goes (everything after the front matter `---`)
- Largest area of the layout
- Automatically populated with your markdown content

### 2. **Secondary (Bottom Left Square)**
- Customize via `secondary_content` in front matter
- Great for: Quick facts, navigation, related links, bio

### 3. **Tertiary (Inner Left Square)**
- Customize via `tertiary_content` in front matter
- Great for: Updates, recent posts, highlights
- Defaults to showing latest blog posts

### 4. **Quinary (Small Bottom Square)**
- Customize via `quinary_content` in front matter
- Great for: Tags, categories, keywords
- Defaults to showing interests/topics

### 5. **Header (Top Area)**
- Automatically includes your name, navigation, and social links
- Customize by editing `_includes/golden-header.html`

## How to Customize a Page

### Basic Usage (uses defaults)
```yaml
---
title: My Page Title
---

# Main Content Here
Your page content...
```

### Custom Secondary Content
```yaml
---
title: My Page Title
secondary_content: |
  ## Custom Sidebar
  - Point 1
  - Point 2
  [Link](/somewhere/)
---

# Main Content Here
```

### Full Customization
```yaml
---
title: My Page Title
secondary_content: |
  ## Custom Section
  Content here...

tertiary_content: |
  ### Another Section
  More content...

quinary_content: |
  **Keywords**
  - Tag 1
  - Tag 2
---

# Main Content Here
```

## Customizing Default Content

To change the default content that appears when you don't specify custom content:

- **Secondary default**: Edit `_includes/golden-secondary.html`
- **Tertiary default**: Edit `_includes/golden-tertiary.html`
- **Quinary default**: Edit `_includes/golden-quinary.html`
- **Header/Navigation**: Edit `_includes/golden-header.html`

## Using a Different Layout

If you want a specific page to NOT use the golden layout:

```yaml
---
layout: page
title: My Page
---
```

Or use any other layout by specifying it in the front matter.

## Mobile Responsive

The layout automatically adapts to mobile screens, stacking the regions vertically for better readability on smaller devices.

## Notes

- All `*_content` fields support full Markdown syntax
- The `| markdownify` filter is automatically applied
- Content is processed through Jekyll's Markdown renderer
- Use `|` after the colon to write multi-line content
