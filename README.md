# Research portfolio

A weekly-updated long/short book, published at <https://mgacoding.github.io>.

## Layout

| Path | What it is |
|---|---|
| `src/portfolio.html` | **The file to edit.** All content lives here. |
| `build.py` | Wraps the source in a full HTML document and adds meta/preview tags. |
| `index.html` | Generated. Do not edit by hand, it gets overwritten. |
| `card.png` | Link preview image (1200x630) used by LinkedIn. |

## Updating the site

Edit `src/portfolio.html`, then:

```
python3 build.py
git add -A && git commit -m "week of <date>" && git push
```

Live in about a minute.

## Custom domain

Add a `CNAME` file at the repo root containing just the domain, set the DNS
records at the registrar, then update `URL` at the top of `build.py` and rebuild
so the preview tags point at the new address.
