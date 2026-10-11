#!/usr/bin/env python3
"""Build general and topic CVs from one format and publication record."""
import os
import argparse
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
VARIANTS = {
    "general": ("Qian_Lou_CV", "Academic CV", None),
    "ai-crypto": ("Qian_Lou_CV_AI_Crypto", "AI and Cryptography CV",
                  {66, 63, 58, 56, 53, 51, 47, 44, 42, 40, 15, 13, 5}),
    "agentic-ai": ("Qian_Lou_CV_Agentic_AI", "Agentic AI CV",
                   {70, 69, 65, 64, 62, 61, 59, 56, 51, 46, 40, 19, 18}),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", choices=VARIANTS, help="Build only this CV (default: all).")
    args = parser.parse_args()
    compiler = os.environ.get("TECTONIC") or shutil.which("tectonic")
    if not compiler:
        raise SystemExit("Set TECTONIC to the path of the tectonic executable.")
    records = (ROOT / "shared/publications.tex").read_text().splitlines()
    pubs = {int(re.match(r"\\cvpub\{\[(\d+)\]", row)[1]): row for row in records if row}
    assert len(pubs) == len(records) and set(pubs) == set(range(1, 71))
    build = ROOT / "build"
    build.mkdir(exist_ok=True)
    shutil.copytree(ROOT / "shared", build / "shared", dirs_exist_ok=True)
    for source in ROOT.glob("*-*.tex"):
        shutil.copy2(source, build / source.name)
    for topic, (name, title, selected) in VARIANTS.items():
        if args.topic and topic != args.topic:
            continue
        url = "https://www.qlou.org/" + ("" if topic == "general" else topic + "/")
        parts = [r"\input{shared/format.tex}",
                 r"\hypersetup{pdftitle={Qian Lou - " + title + "}}",
                 r"\begin{document}", r"\cvheader{" + url + "}",
                 r"\input{" + topic + "-profile.tex}"]
        parts += [r"\input{shared/" + section + ".tex}" for section in ["background", "awards", "grants"]]
        parts += [r"\input{" + topic + "-impact.tex}", r"\input{shared/patents.tex}"]
        groups = [("Publications", set(pubs))] if topic == "general" else [
            ("Selected " + title.removesuffix(" CV") + " Publications", selected),
            ("Additional Publications", set(pubs) - selected),
        ]
        for heading, ids in groups:
            parts.append(r"\cvsection{" + heading + "}")
            parts.append(r"{\footnotesize\itshape * Students and staff under my supervision."
                         + (" Original publication numbers are retained." if topic != "general" else "") + r"\par}\vspace{3pt}")
            parts.extend(pubs[i] for i in sorted(ids, reverse=True))
        parts += [r"\input{shared/professional.tex}", r"\end{document}"]
        source = build / (name + ".tex")
        source.write_text("\n".join(parts) + "\n")
        subprocess.run([compiler, "--keep-logs", "--outdir", str(build), str(source)], cwd=ROOT, check=True)
        shutil.copy2(build / (name + ".pdf"), ROOT.parent / "files" / (name + ".pdf"))


if __name__ == "__main__":
    main()
