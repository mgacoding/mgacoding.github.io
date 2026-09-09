#!/usr/bin/env python3
"""Build site/index.html (deployable) from portfolio.html (the artifact source)."""
import os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(ROOT, "portfolio.html")
OUT  = os.path.join(ROOT, "site", "index.html")

# Set this to your custom domain once you have one, e.g. "https://mairagupta.com"
URL   = "https://mgacoding.github.io"
TITLE = "Maira Gupta | Research portfolio"
DESC  = "A long/short book, updated weekly. Seven positions, each with the numbers behind it."

src = open(SRC).read()
src = src.replace('<style>\n:root{', '<style>\nhtml,body{margin:0}\n:root{', 1)

head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{DESC}">
<meta name="author" content="Maira Gupta">
<link rel="canonical" href="{URL}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Maira Gupta">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}/">
<meta property="og:image" content="{URL}/card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{URL}/card.png">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 fill=%22%231D4E89%22/><text y=%22.9em%22 x=%2250%22 text-anchor=%22middle%22 font-size=%2268%22 font-family=%22Helvetica,sans-serif%22 font-weight=%22bold%22 fill=%22white%22>M</text></svg>">
<style>*{{box-sizing:border-box}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
'''

i = src.index('<nav class="nav"')
out = head + src[:i] + "</head>\n<body>\n" + src[i:] + "\n</body>\n</html>\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(out)

# sanity checks
assert out.count("—") == 0, "em dash found"
assert "<title>" in out and "</html>" in out
print(f"built {OUT}  ({len(out):,} chars)")
