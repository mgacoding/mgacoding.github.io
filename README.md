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

## DNS records for a custom domain

Verified live against GitHub Pages. At the registrar, for the apex (`mairagupta.me`):

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | mgacoding.github.io |

Optional IPv6 (AAAA on `@`): `2606:50c0:8000::153`, `2606:50c0:8001::153`,
`2606:50c0:8002::153`, `2606:50c0:8003::153`.

Once those resolve, run `./set-domain.sh mairagupta.me` and tick **Enforce HTTPS**
in Settings > Pages.
