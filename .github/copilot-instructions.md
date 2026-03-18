# Copilot Instructions

## This project

Jekyll site for Kevin Leander's academic publications, hosted on GitHub Pages.
Source files are in `docs/`. The site uses the Just the Docs theme.

## Running the web server

When Kevin says "run the webserver" or "start Jekyll" or "serve the site", run:

```bash
cd docs && bundle exec jekyll serve
```

The site will be at http://127.0.0.1:4000/

## Key files

- `docs/_config.yml` — site configuration and theme settings
- `docs/index.md` — home page
- `docs/about.md` — bio page
- `docs/*.md` — one file per publications section

## Theme

Just the Docs. Navigation order is controlled by `nav_order:` in each page's front matter.

## Deployment

Push to `main` — GitHub Pages builds and deploys automatically from the `docs/` folder.
