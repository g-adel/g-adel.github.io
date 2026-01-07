# g-adel.github.io

Personal website for Gamal Adel - PhD Candidate in Complex Networks

## Site Structure

This Jekyll site uses a custom **Golden Ratio Layout** as the default for all pages. The layout features a mathematically-proportioned design with multiple customizable regions.

### Golden Layout

The golden layout (`_layouts/golden.html`) is automatically applied to all pages. Each page can customize different regions through front matter or include files.

See [LAYOUT-GUIDE.md](LAYOUT-GUIDE.md) for details on customizing the layout for different pages.

## Generative Art Gallery

The site includes an automated generative art gallery system using Jekyll collections.

### Structure

```
_generative/
  ├── ProjectName/
  │   ├── index.md          # Project description
  │   ├── ProjectName_1.png # Media files
  │   ├── ProjectName_2.mp4
  │   └── ...
  ├── AnotherProject/
  │   ├── index.md
  │   └── AnotherProject_1.png
  └── ...
```

### Adding New Projects

1. **Create a folder** in `_generative/` with your project name (e.g., `_generative/Spirals/`)

2. **Add an index.md file** with project metadata:
   ```yaml
   ---
   title: Spirals
   description: Brief one-line description
   ---
   
   Detailed project description and explanation here.
   ```

3. **Add media files** following the naming convention `ProjectName_#.ext`:
   - `Spirals_1.png`
   - `Spirals_2.mp4`
   - `Spirals_3.gif`
   - etc.

4. **That's it!** Jekyll will automatically:
   - Create a page at `/generative/spirals/`
   - Add it to the gallery at `/generative/`
   - Include it in the sidebar navigation on other project pages
   - Display all files in numerical order

### Supported File Types

- Images: `.png`, `.jpg`, `.jpeg`, `.gif`
- Videos: `.mp4`, `.webm`

### How It Works

The system uses:
- **Jekyll Collections** to manage projects
- **`site.static_files`** to auto-discover media files in each project folder
- **Liquid templates** to dynamically generate galleries and navigation

No manual configuration or data files needed - just add folders and files!

## Development

### Running Locally

```bash
bundle exec jekyll serve
```

**Note:** If you modify `_config.yml`, you must restart the Jekyll server for changes to take effect.

### Building for Production

```bash
bundle exec jekyll build
```

The site will be generated in the `_site/` directory.

## Migration Notes

If migrating from the old generative art structure, run:

```powershell
.\move-generative-files.ps1
```

Then delete the old files and folders as indicated by the script.
