# Docs Jekyll site

This folder contains a minimal Jekyll site for GitHub Pages. To publish this repository as a GitHub Pages site that uses these files, set the Pages source to "main" branch and the "/docs" folder in your repository Settings.

Local testing

Install dependencies (requires Ruby and Bundler):

```bash
bundle install
bundle exec jekyll serve --source docs --watch
```

This will serve the site at http://127.0.0.1:4000. Edit files under `docs/` and refresh.

Publishing on GitHub

- Go to the repository Settings → Pages.
- Under "Source" choose the `main` branch and `/docs` folder, then Save.
- GitHub will build the site with Jekyll and publish it.
