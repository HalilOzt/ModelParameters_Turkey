from __future__ import annotations

import csv
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]


def rows(rel: str) -> list[dict[str, str]]:
    with (ROOT / rel).open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


sources = rows("data/sources_updated.csv")
params = rows("data/parameter_dictionary_updated.csv")
estimates = rows("data/household_preferences_estimates.csv")

source_ids = {r["source_id"] for r in sources}
param_ids = {r["parameter_id"] for r in params}
assert len(source_ids) == len(sources), "Duplicate source_id"
assert len(param_ids) == len(params), "Duplicate parameter_id"
assert len({r["estimate_id"] for r in estimates}) == len(estimates), "Duplicate estimate_id"
assert all(r["source_id"] in source_ids for r in estimates), "Broken source foreign key"
assert all(r["parameter_id"] in param_ids for r in estimates), "Broken parameter foreign key"
assert all(r["verification_status"] == "pdf_verified" for r in estimates)

for field in ("value", "lower_bound", "upper_bound", "standard_error"):
    for r in estimates:
        if r[field]:
            float(r[field])

source_map = {r["source_id"]: r for r in sources}
page_cache: dict[Path, int] = {}
for r in estimates:
    src = source_map[r["source_id"]]
    pdf = ROOT / src["local_pdf"]
    assert pdf.exists(), f"Missing PDF: {pdf}"
    if pdf not in page_cache:
        page_cache[pdf] = len(PdfReader(str(pdf)).pages)
    page = int(r["source_pdf_page"])
    assert 1 <= page <= page_cache[pdf], f"Page out of range: {r['estimate_id']}"

checksums = (ROOT / "sources/pdfs/SHA256SUMS.txt").read_text(encoding="utf-8-sig").splitlines()
pdf_names = {p.name for p in (ROOT / "sources/pdfs").glob("*.pdf")}
checksum_names = {line.split("  ", 1)[1] for line in checksums if "  " in line}
assert pdf_names == checksum_names, "Checksum inventory does not match PDF inventory"

print(
    f"OK sources={len(sources)} parameters={len(params)} "
    f"household_estimates={len(estimates)} pdfs={len(pdf_names)} "
    f"household_source_pdfs_checked={len(page_cache)}"
)
