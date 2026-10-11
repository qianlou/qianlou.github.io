"""Build the AI Safety and Security page; reuse homepage records and topic styling.

Run: python3 scripts/build-ai-safety.py
Edit scripts/templates/ai-safety.html for the research narrative.
"""
from html import escape, unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "index.html").read_text()
template = (ROOT / "scripts/templates/ai-safety.html").read_text()
papers = {
    "RealM:": ("realm", None),
    "PRO:": ("pro", None),
    "Evaluating LLM Watermarking for Clinical EHR:": ("clinical-ehr", None),
    "MemIncept:": ("memincept", None),
    "Conjunctive Prompt Attacks": ("conjunctive", None),
    "SecureRoute:": ("secureroute", "https://arxiv.org/pdf/2604.15499"),
    "SIF:": ("sif", None),
    "FHE-Coder:": ("fhe-coder", "https://openreview.net/pdf?id=4F1py5vQXm"),
    "Factuality Beyond Coherence:": ("factuality", None),
    "Evaluating the Robustness and Accuracy of Text Watermarking": ("crosslingual", None),
    "DataSeal:": ("dataseal", "https://arxiv.org/pdf/2410.15215"),
    "CR-UTP:": ("cr-utp", "https://aclanthology.org/2024.findings-acl.588.pdf"),
    "SSL-Cleanse:": ("ssl-cleanse", "https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/11933.pdf"),
    "TrojLLM:": ("trojllm", "https://proceedings.neurips.cc/paper_files/paper/2023/file/cf04d01a0e76f8b13095349d9caca033-Paper-Conference.pdf"),
    "TrojText:": ("trojtext", "https://openreview.net/pdf?id=ja4Lpp5mqc2"),
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
    'Support across my research program spans AI security, private computing, healthcare AI, and education. The DoD Pathfinder project addresses LLM security testing; NSF CAREER and SaTC support secure infrastructure and privacy-preserving data synthesis. Other awards support complementary research and workforce development.')
output = template.replace('<!-- SHARED_PROFILE -->', profile_html)
output = output.replace('<!-- SELECTED_PUBLICATIONS -->', '\n\n'.join(entries))
output = output.replace('<!-- SHARED_FUNDING -->', funding_html)
destination = ROOT / 'ai-safety/index.html'
destination.parent.mkdir(exist_ok=True)
destination.write_text(output)
print(f"Built {destination.relative_to(ROOT)} with {len(entries)} publications")
