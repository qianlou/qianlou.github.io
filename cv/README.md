# Shared Academic CVs

Both PDFs use `shared/format.tex` for Palatino typography, blue section headings,
margins, spacing, contact header, grants, and citation layout.

Build with `TECTONIC=/path/to/tectonic python3 cv/build.py` from the repository root.
Generated PDFs are copied to `files/`; intermediate files remain in ignored `cv/build/`.

Edit common factual information in `shared/`. Profiles, open-source highlights,
and research contributions are in the `general-*` and `ai-crypto-*` files.
Publications have one shared record. Numbers 1-63 preserve the previous CV;
64-70 add the seven NeurIPS/EMNLP 2026 papers already listed on the homepage.
The AI/Crypto CV highlights selected papers first, then includes every remaining
publication without duplication or renumbering. Author underlining, venue bolding,
and supervision stars are preserved.

To add a future topic, reuse the shared format and factual records rather than
copying and independently modifying them. Update the expected publication ID
range in `build.py` when adding publications.
