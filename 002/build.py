#!/usr/bin/env python3
"""반반_완성본.md → ../docs/002/index.html 변환."""
import html
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "반반_완성본.md"
OUT = HERE.parent / "docs" / "002" / "index.html"

text = SRC.read_text(encoding="utf-8").strip()
lines = text.split("\n")
title = lines[0].lstrip("# ").strip()
body = "\n".join(lines[1:]).strip()
paras = [p.strip() for p in body.split("\n\n") if p.strip()]
paras_html = "\n".join(f"      <p>{html.escape(p)}</p>" for p in paras)

page = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — 반반 단편</title>
<meta name="description" content="단편소설 {html.escape(title)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;600&family=Nanum+Myeongjo:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #faf7f2;
    --paper: #fffdf9;
    --ink: #2b2722;
    --muted: #8a8074;
    --accent: #9a6a4f;
    --rule: #e4dcd0;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #16140f;
      --paper: #1d1a14;
      --ink: #e6ded2;
      --muted: #8d8374;
      --accent: #c89a7e;
      --rule: #34302a;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: "Noto Serif KR", "Nanum Myeongjo", serif;
    line-height: 2.05;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
  }}
  .sheet {{
    max-width: 42rem;
    margin: 0 auto;
    padding: 5rem 1.5rem 7rem;
    background: var(--paper);
    min-height: 100vh;
    box-shadow: 0 0 60px rgba(0,0,0,.04);
  }}
  header {{ text-align: center; margin-bottom: 4.5rem; }}
  .hanja {{
    display: block;
    font-size: .95rem;
    letter-spacing: .9em;
    margin-left: .9em;
    color: var(--accent);
    margin-bottom: 1.2rem;
  }}
  h1 {{
    font-size: 2.3rem;
    font-weight: 600;
    letter-spacing: .35em;
    margin: 0 0 1.6rem;
    margin-left: .35em;
  }}
  .byline {{
    color: var(--muted);
    font-size: .95rem;
    letter-spacing: .25em;
  }}
  .byline::before, .byline::after {{
    content: "—";
    color: var(--rule);
    margin: 0 .8em;
  }}
  hr.orn {{
    border: 0;
    margin: 3rem auto 0;
    width: 5rem;
    border-top: 1px solid var(--rule);
    position: relative;
  }}
  hr.orn::after {{
    content: "半";
    position: absolute;
    top: -0.85em;
    left: 50%;
    transform: translateX(-50%);
    background: var(--paper);
    padding: 0 .6em;
    color: var(--accent);
    font-size: .85rem;
  }}
  article p {{
    margin: 0 0 1.9rem;
    text-indent: 1em;
    word-break: keep-all;
    overflow-wrap: break-word;
    font-size: 1.06rem;
  }}
  article p:first-of-type::first-letter {{
    font-size: 1.9em;
    line-height: 1;
    color: var(--accent);
    font-weight: 600;
  }}
  footer {{
    margin-top: 5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--rule);
    text-align: center;
    color: var(--muted);
    font-size: .85rem;
    letter-spacing: .15em;
  }}
  @media (max-width: 600px) {{
    .sheet {{ padding: 3.5rem 1.25rem 5rem; }}
    h1 {{ font-size: 1.8rem; }}
    article p {{ font-size: 1.02rem; line-height: 1.95; }}
  }}
</style>
</head>
<body>
  <div class="sheet">
    <header>
      <span class="hanja">短篇小說</span>
      <h1>{html.escape(title.split('(')[0])}</h1>
      <div class="byline">반반</div>
      <hr class="orn">
    </header>
    <article>
{paras_html}
    </article>
    <footer>半半 · 끝</footer>
  </div>
</body>
</html>
"""
OUT.write_text(page, encoding="utf-8")
print(f"wrote {OUT} ({len(page)} chars, {len(paras)} paragraphs)")
