#!/usr/bin/env python3
"""Redact 'April 2026' on page 1 of the internship PDF (title slide). Requires pymupdf."""

import sys

import fitz


def main():
    if len(sys.argv) != 3:
        print("Usage: redact_report_title_date.py input.pdf output.pdf", file=sys.stderr)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    doc = fitz.open(src)
    page = doc[0]
    for r in page.search_for("April 2026"):
        page.add_redact_annot(r, fill=(1, 1, 1))
    page.apply_redactions()
    doc.save(dst, garbage=4, deflate=True)
    doc.close()


if __name__ == "__main__":
    main()
