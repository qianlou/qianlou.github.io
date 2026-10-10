"""Build the topic page from its template and the main homepage's shared records.

Run: python3 scripts/build-ai-crypto.py
Edit scripts/templates/ai-crypto.html for topic prose. Author lists, venues, and
the profile/contact block are read from index.html to avoid duplicate records.
"""

from html import escape, unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "index.html").read_text()
template = (ROOT / "scripts/templates/ai-crypto.html").read_text()

# Keep the homepage ordering within each publication year.
papers = {
    "CipherFlow:": ("cipherflow", None),
    "FHAIM:": ("fhaim", "https://arxiv.org/pdf/2602.05838"),
    "Efficient Arithmetic-and-Comparison Homomorphic Encryption": (
        "universal-bgv", "https://arxiv.org/pdf/2604.19890"),
    "SecureRoute:": ("secureroute", "https://arxiv.org/pdf/2604.15499"),
    "ReliaFHE:": ("reliafhe", "https://dl.acm.org/doi/10.1145/3779212.3790211"),
    "FHE-Coder:": ("fhe-coder", "https://openreview.net/pdf?id=4F1py5vQXm"),
    "DictPFL:": ("dictpfl", "https://arxiv.org/pdf/2510.21086"),
    "zkVC:": ("zkvc", "https://arxiv.org/pdf/2504.12217"),
    "CipherPrune:": ("cipherprune", "https://arxiv.org/pdf/2502.16782"),
    "DataSeal:": ("dataseal", "https://arxiv.org/pdf/2410.15215"),
    "HEMET:": ("hemet", "https://arxiv.org/pdf/2106.00038"),
    "SAFENet:": ("safenet", "https://openreview.net/pdf?id=Cz3dbFm5u-"),
    "SHE:": ("she", "https://proceedings.neurips.cc/paper_files/paper/2019/file/56a3107cad6611c8337ee36d178ca129-Paper.pdf"),
}

profile = re.search(r'<div class="profiletop">.*?</div>\s*</div>', source, re.S)
if profile is None:
    raise ValueError("Could not find the homepage profile block")
profile_html = profile.group().replace('src="images/', 'src="../images/')
profile_html = profile_html.replace('width="250px"', 'width="250"')

entries = []
found = set()
for table in re.findall(r'<table class="imgtable pubentry">.*?</table>', source, re.S):
    plain = unescape(re.sub(r'<[^>]+>', '', table))
    for title, (slug, paper_url) in papers.items():
        if title not in plain:
            continue
        if title in found:
            raise ValueError(f"Duplicate publication: {title}")
        found.add(title)
        entry = table.replace('<table ', f'<table id="pub-{slug}" ', 1)
        # Preserve the title, author order, supervision markers, and venue.
        # Replace old resource links with direct paper links where available.
        venue_end = entry.index('</i>') + len('</i>')
        entry = entry[:venue_end].rstrip()
        if paper_url:
            label = "Publisher" if "dl.acm.org" in paper_url else "Paper (PDF)"
            entry += f'<br />[<a href="{escape(paper_url, quote=True)}">{label}</a>]'
        entry += '\n</p></td></tr></table>'
        entries.append(entry)

missing = set(papers) - found
if missing:
    raise ValueError(f"Missing publication records: {sorted(missing)}")

output = template.replace('<!-- SHARED_PROFILE -->', profile_html)
output = output.replace('<!-- SELECTED_PUBLICATIONS -->', '\n\n'.join(entries))
destination = ROOT / 'ai-crypto/index.html'
destination.parent.mkdir(exist_ok=True)
destination.write_text(output)
print(f"Built {destination.relative_to(ROOT)} with {len(entries)} publications")
