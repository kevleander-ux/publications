# Kevin Leander — Publications Site

This folder contains the Jekyll site published via GitHub Pages.

> **Note:** This README file is intentionally ignored by Jekyll and will not appear on the website. Use it freely for notes and instructions.

---

## Serving the site locally

From the **project root** (not the `docs/` folder):

```bash
bundle exec jekyll serve --source docs
```

The site will be available at http://127.0.0.1:4000/

To stop the server, press `Ctrl+C`.

If you haven't installed dependencies yet:

```bash
bundle install
```

---

## Changing the theme skin (Minimal Mistakes)

The current theme is **Minimal Mistakes**. You can change the look by editing one line in `docs/_config.yml`.

Find this section and add or change the `minimal_mistakes_skin` line:

```yaml
minimal_mistakes_skin: "default"
```

Available skins:

| Skin name   | Look                          |
|-------------|-------------------------------|
| `default`   | White with blue accents       |
| `mint`      | Clean with green accents      |
| `contrast`  | High-contrast black and white |
| `dark`      | Dark background               |
| `sunrise`   | Warm tones, orange accents    |
| `dirt`      | Earthy, muted tones           |
| `neon`      | Dark with bright accents      |
| `air`       | Light, airy blue-grey         |
| `aqua`      | Teal and aqua tones           |

After saving `_config.yml`, restart the local server to see the change. On GitHub Pages, push the change and wait ~1 minute for it to rebuild.

---

## Publishing on GitHub Pages

- Go to the repository **Settings → Pages**
- Under "Source" choose the `main` branch and `/docs` folder, then Save
- GitHub will build the site automatically on every push to `main`

---

## Theme branches

This repo has branches for comparing different themes:

- `main` — Minimal Mistakes (current)
- `just-the-docs` — Just the Docs theme (sidebar navigation)
- `mm-skin` — Minimal Mistakes with the `mint` skin

To switch to a different theme, merge the desired branch into `main`.
