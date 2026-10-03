# Per-format tips

## Contents
- PDF · DOCX · XLSX/XLS · PPTX · HTML/URL · CSV/JSON/XML · Images · Audio · ZIP · YouTube

## PDF
- Works only on PDFs with a text layer. Scanned PDFs return empty/near-empty output; no OCR by default. Tell the user and suggest OCR or `-d` (Azure Document Intelligence) if they have it.
- Expect hard line wraps mid-sentence, repeated headers/footers and page numbers, and flattened tables. Re-join lines and rebuild tables by hand.
- Multi-column layouts can interleave columns; compare against the original when the text reads oddly.

## DOCX
- Best-supported format: headings, lists, bold/italic, and tables are preserved.
- Embedded images are not extracted (data URIs are truncated unless `--keep-data-uris`). Ask for the original images if they're needed.

## XLSX / XLS
- One Markdown table per sheet, headed by the sheet name. Formulas show computed values.
- For large sheets, convert then read only the needed sheet/rows; or use pandas directly for real analysis.

## PPTX
- Output is per slide, with titles, text, tables, and notes. Charts and SmartArt may be missing; images get their alt text if present.

## HTML / URL
- Pages convert to readable Markdown, but navigation, cookie banners, and footers come along. Trim them.
- Some sites block non-browser fetches or render with JavaScript; if the output is empty, fetch the page another way.

## CSV / JSON / XML
- CSV becomes a table. JSON/XML are emitted as text, so there's little benefit over reading them directly.

## Images
- EXIF metadata only by default. Captions/OCR need an LLM client (see REFERENCE.md); don't enable unless asked.

## Audio
- Metadata plus speech transcription, which needs extra dependencies and network access to a speech service.

## ZIP
- Each contained file is converted and concatenated; for many files, extract and use `scripts/convert.py` instead.

## YouTube
- Returns title, description, and transcript when available.
