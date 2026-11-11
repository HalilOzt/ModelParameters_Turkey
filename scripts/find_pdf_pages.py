from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Find PDF pages containing a text fragment.")
    parser.add_argument("input", type=Path)
    parser.add_argument("query")
    args = parser.parse_args()

    reader = PdfReader(str(args.input))
    query = args.query.casefold()
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if query in text.casefold():
            compact = " ".join(text.split())
            print(f"{page_number}\t{compact[:500]}")


if __name__ == "__main__":
    main()
