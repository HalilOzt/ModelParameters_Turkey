from __future__ import annotations

import csv
import json
import shutil
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


SITE = Path(__file__).resolve().parent
ROOT = SITE.parents[1]
DATA = ROOT / "data"
DIST = SITE / "dist"

SOURCE_FILE = DATA / "sources_updated.csv"
PARAMETER_FILE = DATA / "parameter_dictionary_updated.csv"
ESTIMATE_FILES = [
    ("production-technology", "Üretim ve Teknoloji", DATA / "production_technology_estimates.csv"),
    ("capital-investment", "Sermaye ve Yatırım", DATA / "capital_investment_estimates_updated.csv"),
    ("pricing-inflation-firms", "Fiyatlama, Enflasyon ve Firmalar", DATA / "pricing_inflation_firms_estimates.csv"),
    ("household-preferences", "Hanehalkı ve Tercihler", DATA / "household_preferences_estimates.csv"),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def number(value: str):
    if value is None or value == "":
        return None
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


sources = read_csv(SOURCE_FILE)
parameters = read_csv(PARAMETER_FILE)
estimates: list[dict] = []

for family_id, family_name, path in ESTIMATE_FILES:
    for row in read_csv(path):
        converted = dict(row)
        for field in ("value", "lower_bound", "upper_bound", "standard_error", "source_pdf_page"):
            converted[field] = number(converted.get(field, ""))
        converted["family_id"] = family_id
        converted["family_name"] = family_name
        estimates.append(converted)

source_map = {row["source_id"]: row for row in sources}
parameter_map = {row["parameter_id"]: row for row in parameters}

missing_sources = sorted({r["source_id"] for r in estimates} - source_map.keys())
missing_parameters = sorted({r["parameter_id"] for r in estimates} - parameter_map.keys())
if missing_sources or missing_parameters:
    raise SystemExit(f"Broken foreign keys: sources={missing_sources}, parameters={missing_parameters}")

param_estimates: dict[str, list[dict]] = defaultdict(list)
source_estimates: dict[str, list[dict]] = defaultdict(list)
for row in estimates:
    param_estimates[row["parameter_id"]].append(row)
    source_estimates[row["source_id"]].append(row)

parameter_index = []
for row in parameters:
    subset = param_estimates.get(row["parameter_id"], [])
    values = [x["value"] for x in subset if isinstance(x["value"], (int, float))]
    families = sorted({x["family_id"] for x in subset})
    parameter_index.append({
        **row,
        "estimate_count": len(subset),
        "source_count": len({x["source_id"] for x in subset}),
        "families": families,
        "min_value": min(values) if values else None,
        "max_value": max(values) if values else None,
        "units": sorted({x["unit"] for x in subset if x["unit"]}),
        "statuses": sorted({x["estimate_status"] for x in subset if x["estimate_status"]}),
    })

source_index = []
for row in sources:
    subset = source_estimates.get(row["source_id"], [])
    source_index.append({
        **row,
        "year": number(row.get("year", "")),
        "pdf_pages": number(row.get("pdf_pages", "")),
        "estimate_count": len(subset),
        "parameter_count": len({x["parameter_id"] for x in subset}),
        "families": sorted({x["family_id"] for x in subset}),
    })

families = []
for family_id, family_name, _ in ESTIMATE_FILES:
    subset = [x for x in estimates if x["family_id"] == family_id]
    families.append({
        "id": family_id,
        "name": family_name,
        "estimate_count": len(subset),
        "parameter_count": len({x["parameter_id"] for x in subset}),
        "source_count": len({x["source_id"] for x in subset}),
    })

verification_counts = Counter(x["verification_status"] for x in estimates)
status_counts = Counter(x["estimate_status"] for x in estimates)

catalog = {
    "meta": {
        "title": "Türkiye Ekonomisi Model Parametreleri",
        "generated_on": date.today().isoformat(),
        "source_count": len(sources),
        "parameter_count": len(parameters),
        "estimate_count": len(estimates),
        "archived_pdf_count": sum(1 for x in sources if x.get("access_status") == "archived"),
        "verification_counts": dict(verification_counts),
        "status_counts": dict(status_counts),
    },
    "families": families,
    "parameters": parameter_index,
    "sources": source_index,
    "estimates": estimates,
}

(DIST / "data").mkdir(parents=True, exist_ok=True)
(DIST / "downloads").mkdir(parents=True, exist_ok=True)
(DIST / "data" / "catalog.json").write_text(
    json.dumps(catalog, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
)

download_files = [SOURCE_FILE, PARAMETER_FILE, *(item[2] for item in ESTIMATE_FILES)]
for source in download_files:
    shutil.copy2(source, DIST / "downloads" / source.name)

print(
    f"Built catalog: {len(sources)} sources, {len(parameters)} parameters, "
    f"{len(estimates)} estimates, {len(families)} families"
)

