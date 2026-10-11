"""Build the Agentic AI topic page; reuse homepage records and topic styling.

Run: python3 scripts/build-agentic-ai.py
Edit scripts/templates/agentic-ai.html for the research narrative.
"""
from html import escape, unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "index.html").read_text()
template = (ROOT / "scripts/templates/agentic-ai.html").read_text()
papers = {
    "Chain-of-Route:": ("chain-of-route", None),
    "Learning Latency-Aware Orchestration": ("orchestration", None),
    "Learning What to Retain:": ("gated-memory", None),
    "Evaluating LLM Watermarking for Clinical EHR:": ("clinical-ehr", None),
    "MemIncept:": ("memincept", None),
    "R2-Router:": ("r2-router", "https://arxiv.org/pdf/2602.02823"),
    "Conjunctive Prompt Attacks": ("conjunctive", None),
    "SecureRoute:": ("secureroute", "https://arxiv.org/pdf/2604.15499"),
    "FHE-Coder:": ("fhe-coder", "https://openreview.net/pdf?id=4F1py5vQXm"),
    "Factuality Beyond Coherence:": ("factuality", None),
    "DataSeal:": ("dataseal", "https://arxiv.org/pdf/2410.15215"),
    "Language model compression with weighted low-rank factorization":
        ("low-rank", "https://arxiv.org/pdf/2207.00112"),
    "DictFormer:": ("dictformer", "https://openreview.net/pdf?id=GWQWAeE9EpB"),
}

profile = re.search(r'<div class="profiletop">.*?</div>\s*</div>', source, re.S)
if not profile:
    raise ValueError("Missing shared homepage profile")
profile_html = profile.group().replace('src="images/', 'src="../images/')
profile_html = profile_html.replace('width="250px"', 'width="250"')

entries, found = [], set()
for table in re.findall(r'<table class="imgtable pubentry">.*?</table>', source, re.S):
    plain = unescape(re.sub(r'<[^>]+>', '', table))
    for title, (slug, url) in papers.items():
        if title not in plain:
            continue
        if title in found:
            raise ValueError(f"Duplicate publication: {title}")
        found.add(title)
        entry = table.replace('<table ', f'<table id="pub-{slug}" ', 1)
        entry = entry[:entry.index('</i>') + len('</i>')].rstrip()
        if url:
            entry += f'<br />[<a href="{escape(url, quote=True)}">Paper (PDF)</a>]'
        entries.append(entry + '\n</p></td></tr></table>')
if set(papers) != found:
    raise ValueError(f"Missing publications: {set(papers) - found}")

# Funding is shared factual information, not a claim that every award funds agents.
funding_source = (ROOT / "scripts/templates/ai-crypto.html").read_text()
funding = re.search(r'<section aria-labelledby="funding">.*?</section>', funding_source, re.S)
if not funding:
    raise ValueError("Missing shared funding section")
funding_html = funding.group().replace(
    'Research and education support spans secure computing, AI systems, healthcare AI, and workforce development.',
    'Support across my research program spans AI systems, healthcare AI, secure computing, and workforce development. The NIH project directly supports the healthcare direction described above; other awards support complementary research and education.')
output = template.replace('<!-- SHARED_PROFILE -->', profile_html)
output = output.replace('<!-- SELECTED_PUBLICATIONS -->', '\n\n'.join(entries))
output = output.replace('<!-- SHARED_FUNDING -->', funding_html)
destination = ROOT / 'agentic-ai/index.html'
destination.parent.mkdir(exist_ok=True)
destination.write_text(output)
print(f"Built {destination.relative_to(ROOT)} with {len(entries)} publications")
