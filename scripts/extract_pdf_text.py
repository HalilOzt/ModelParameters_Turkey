from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract page-delimited UTF-8 text from PDFs.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--start", type=int, default=1, help="First page, one-based and inclusive")
    parser.add_argument("--end", type=int, help="Last page, one-based and inclusive")
    args = parser.parse_args()

    reader = PdfReader(str(args.input))
    start = max(args.start, 1)
    end = min(args.end or len(reader.pages), len(reader.pages))
    if start > end:
        raise SystemExit(f"Invalid page range: {start}-{end} for {len(reader.pages)} pages")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as stream:
        for page_number in range(start, end + 1):
            text = reader.pages[page_number - 1].extract_text() or ""
            stream.write(f"\n===== PDF PAGE {page_number} =====\n")
            stream.write(text)
            stream.write("\n")


if __name__ == "__main__":
    main()
