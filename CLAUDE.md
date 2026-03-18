# Claude Code Instructions

## This project

Jekyll site for Kevin Leander's academic publications, hosted on GitHub Pages.
Source files are in `docs/`. The site uses the Just the Docs theme.

## Running the web server

When Kevin says "run the webserver" or "start Jekyll" or "serve the site":

```bash
cd docs && bundle exec jekyll serve
```

The site will be at http://127.0.0.1:4000/

## Key files

- `docs/_config.yml` — site configuration and theme settings
- `docs/index.md` — home page
- `docs/about.md` — bio page
- `docs/digital-literacies-and-ai.md` — publications section
- `docs/affect-and-embodiment.md` — publications section
- `docs/space-and-time.md` — publications section
- `docs/positioning-and-identity.md` — publications section
- `docs/posthumanisms.md` — publications section

## Theme

Just the Docs. Navigation order is controlled by `nav_order:` in each page's front matter.
To change the look, see the Just the Docs documentation for color schemes and configuration.

## Deployment

Push to `main` branch — GitHub Pages builds and deploys automatically from the `docs/` folder.
