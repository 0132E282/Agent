#!/usr/bin/env python3
"""Batch-convert files or folders to Markdown with markitdown.

Usage:
    python convert.py INPUT [INPUT ...] -o OUTDIR [--ext .pdf,.docx] [--overwrite]

Each input file becomes OUTDIR/<name>.md. Folders are walked recursively.
Requires: uv tool install "markitdown[all]"  (or pip install "markitdown[all]")
"""
import argparse
import sys
from pathlib import Path

DEFAULT_EXTS = {".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".html", ".htm",
                ".csv", ".epub", ".zip"}


def collect(inputs, exts):
    for p in map(Path, inputs):
        if p.is_dir():
            yield from (f for f in sorted(p.rglob("*"))
                        if f.is_file() and f.suffix.lower() in exts)
        elif p.is_file():
            yield p
        else:
            print(f"skip (not found): {p}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="files or folders")
    ap.add_argument("-o", "--outdir", required=True, help="output directory (outside the repo)")
    ap.add_argument("--ext", help="comma-separated extensions to include for folders, e.g. .pdf,.docx")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    try:
        from markitdown import MarkItDown
    except ImportError:
        sys.exit('markitdown not importable. Install: pip install "markitdown[all]" '
                 '(the uv tool install is CLI-only; use `markitdown FILE` instead).')

    exts = {e if e.startswith(".") else f".{e}" for e in args.ext.lower().split(",")} \
        if args.ext else DEFAULT_EXTS
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    md = MarkItDown()
    ok = fail = 0
    for f in collect(args.inputs, exts):
        dest = out / f"{f.stem}.md"
        if dest.exists() and not args.overwrite:
            print(f"skip (exists): {dest}")
            continue
        try:
            text = md.convert(str(f)).text_content
            dest.write_text(text, encoding="utf-8")
            print(f"ok   {f} -> {dest} ({len(text)} chars)")
            ok += 1
        except Exception as e:  # keep going on bad files
            print(f"FAIL {f}: {e}", file=sys.stderr)
            fail += 1
    print(f"done: {ok} converted, {fail} failed")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
