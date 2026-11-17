"""Render spec diagrams and a sibling HTML report with Python and Graphviz dot."""
import base64
from html import escape
from pathlib import Path
import re
import subprocess

here = Path(__file__).resolve().parent
repo = here.parents[3]
out = repo.parent / 'meridian-report' / 'index.html'
out.parent.mkdir(exist_ok=True)
sections = []
nav = []
for key, edges in re.findall(r'digraph (\w+) \{(.*?)\n\}', (here / 'flows.dot').read_text(), re.S):
    source = 'digraph G {\ngraph [bgcolor="transparent", pad=.2]; node [shape=box,style="rounded,filled",color="#548782",fillcolor="#edf6f4",fontname="Helvetica"]; edge [color="#416864",fontname="Helvetica",fontsize=11];\n' + edges + '\n}'
    svg = subprocess.check_output(['dot', '-Tsvg'], input=source.encode())
    (here / f'{key}.svg').write_bytes(svg)
    spec = (here.parent / 'specs' / f'{key}.md').read_text()
    title = escape(spec.splitlines()[0].removeprefix('# '))
    diagram = re.search(r'!\[([^\]]+)\]\(\.\./flows/[^)]+\)\n\n([^\n]+)', spec)
    status, caption = map(escape, diagram.groups())
    src = base64.b64encode(svg).decode()
    nav.append(f'<a href="#{key}">{title}</a>')
    sections.append(f'<section id="{key}"><small>{status}</small><h2>{title}</h2><p>{caption}</p><img alt="{title} flow diagram" src="data:image/svg+xml;base64,{src}"></section>')

out.write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Meridian | Decision report</title>
<style>*{box-sizing:border-box}body{max-width:850px;margin:auto;padding:2rem 1rem;background:#faf9f5;color:#193a38;font:17px/1.5 system-ui}h1,h2{line-height:1.15}header,section{background:white;border:1px solid #ccdcd8;padding:clamp(1rem,4vw,2.3rem);margin:1rem 0;border-radius:12px}small{color:#365f59;text-transform:uppercase;letter-spacing:.09em}nav a{display:inline-block;margin:.25em .8em .25em 0;color:#1d6057}img{display:block;max-width:100%;height:auto;margin:1rem auto}section{break-inside:avoid}@media print{nav{display:none}body{padding:0}}</style>
<header><small>Meridian Exchange / design notebook</small><h1>When yesterday’s fix no longer fits</h1><p>We chose Meridian so we can study how agents use information. The simulator supplies incidents and records what happened.</p>
<h2>What we agreed</h2><p>Compare three shifts: first discovery, recurrence, then the same alert with a different cause. Run each sequence with memory off and on.</p>
<p>Count verified successes per case. Did recall save investigation calls? Did the decisive clue reach the agent? Did the cache avoid a read or return stale information? Include the cost of writing, retrieving, and correcting memory.</p>
<p>A data leak, unauthorized action, duplicate effect, or unsupported recovery claim blocks adoption, even if the run costs less.</p>
<p>The diagrams show proposed behavior except for the agreed evaluation comparison. Project results are still pending.</p></header><nav aria-label="Contents">''' + ' '.join(nav) + '</nav>' + ''.join(sections) + '</html>')
print(out)
