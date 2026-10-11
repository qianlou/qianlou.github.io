"""Build the AI Infrastructure topic page; reuse homepage records and topic styling.

Run: python3 scripts/build-ai-infra.py
Edit scripts/templates/ai-infra.html for the research narrative.
"""
from html import escape, unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "index.html").read_text()
template = (ROOT / "scripts/templates/ai-infra.html").read_text()
papers = {
    "Chain-of-Route:": ("chain-of-route", None),
    "Learning Latency-Aware Orchestration": ("orchestration", "https://arxiv.org/pdf/2607.13359"),
    "CipherFlow:": ("cipherflow", None),
    "HBM-CASO:": ("hbm-caso", None),
    "HW-Router:": ("hw-router", None),
    "ReliaFHE:": ("reliafhe", "https://dl.acm.org/doi/10.1145/3779212.3790211"),
    "R2-Router:": ("r2-router", "https://arxiv.org/pdf/2602.02823"),
    "Lite-MDETR:": ("lite-mdetr", "https://openaccess.thecvf.com/content/CVPR2022/papers/Lou_Lite-MDETR_A_Lightweight_Multi-Modal_Detector_CVPR_2022_paper.pdf"),
    "MATCHA:": ("matcha", "https://arxiv.org/pdf/2202.08814"),
    "AutoQ:": ("autoq", "https://arxiv.org/pdf/1902.05690"),
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
            label = "Publisher" if "dl.acm.org" in url else "Paper (PDF)"
            entry += f'<br />[<a href="{escape(url, quote=True)}">{label}</a>]'
        entries.append(entry + '\n</p></td></tr></table>')
if set(papers) != found:
    raise ValueError(f"Missing publications: {set(papers) - found}")

# Reuse funding records without implying every award funds this topic.
funding_source = (ROOT / "scripts/templates/ai-crypto.html").read_text()
funding = re.search(r'<section aria-labelledby="funding">.*?</section>', funding_source, re.S)
if not funding:
    raise ValueError("Missing shared funding section")
funding_html = funding.group().replace(
    'Research and education support spans secure computing, AI systems, healthcare AI, and workforce development.',
    'Support across my research program spans AI infrastructure, secure computing, healthcare AI, and education. Amazon-supported work addresses compression and post-training; NSF CAREER and CISE Core support secure computing infrastructure. Other awards support complementary applications and workforce development.')
output = template.replace('<!-- SHARED_PROFILE -->', profile_html)
output = output.replace('<!-- SELECTED_PUBLICATIONS -->', '\n\n'.join(entries))
output = output.replace('<!-- SHARED_FUNDING -->', funding_html)
destination = ROOT / 'ai-infra/index.html'
destination.parent.mkdir(exist_ok=True)
destination.write_text(output)
print(f"Built {destination.relative_to(ROOT)} with {len(entries)} publications")
