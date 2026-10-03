# markitdown reference

## Contents
- CLI flags · Python API · Optional extras · Environment variables

## CLI flags (v0.1.8)

| Flag | Purpose |
|---|---|
| `FILENAME` | Input file or URL; omit to read stdin |
| `-o, --output FILE` | Write to file instead of stdout |
| `-x, --extension EXT` | Extension hint for stdin (e.g. `.pdf`) |
| `-m, --mime-type TYPE` | MIME type hint |
| `-c, --charset CS` | Charset hint (e.g. `UTF-8`) |
| `-d, --use-docintel` | Use Azure Document Intelligence (needs `-e ENDPOINT`) |
| `-e, --endpoint URL` | Document Intelligence endpoint |
| `--use-cu` / `--cu-endpoint` / `--cu-analyzer` / `--cu-file-types` | Azure Content Understanding routing |
| `-p, --use-plugins` | Enable 3rd-party plugins (runs third-party code) |
| `--list-plugins` | List installed plugins |
| `--keep-data-uris` | Keep base64 images instead of truncating |

Run `markitdown --help` for the installed version's exact flags.

## Python API

```python
from markitdown import MarkItDown

md = MarkItDown()                       # offline, no plugins
result = md.convert("report.docx")      # path, URL, or file-like object
print(result.text_content)
```

With an LLM for image descriptions (only if the user asks and provides a key):

```python
from openai import OpenAI
md = MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")
```

## Optional extras

Install selectively: `uv tool install "markitdown[pdf,docx,pptx,xlsx]"`, or everything with `[all]`.
Others: `xls`, `outlook`, `audio-transcription`, `youtube-transcription`, `az-doc-intel`.

## Environment variables

- `MARKITDOWN_DOCINTEL_ENDPOINT` — default endpoint for `-d`
- `MARKITDOWN_CU_ENDPOINT` — default endpoint for `--use-cu`

## Upgrade

```bash
uv tool upgrade markitdown
```
