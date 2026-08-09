[![中文](https://img.shields.io/badge/中文-文档-blue)](VALIDATION.zh.md)

# Validation evidence

Validation was performed from a clean temporary copy and a newly created virtual environment. The evidence is bound to implementation commit `340b8943106bdc3c248f40748ee817c08ceba881`.

## Environment

- Windows host with Python 3.12.13.
- Sphinx 4.5.0 and the exact dependencies in `docs/requirements.txt`.
- A clean dependency installation was used; no repository-local environment was reused.

## Results

| Check | Result |
| --- | --- |
| Source/catalog alignment | 26 `.rst`, 26 `.po`, and 26 `.mo` files |
| Translation coverage | 1,425 of 1,425 current messages have non-empty translations; 0 missing, 0 fuzzy, 0 UTF-8 BOM files |
| Catalog compilation | Passed for all 26 catalogs, 0 warnings |
| Chinese HTML, strict mode | Passed, 28 pages, 0 warnings/errors |
| English HTML, strict mode | Passed, 28 pages, 0 warnings/errors |
| LaTeX source, strict mode | Passed, one `.tex` output, 0 warnings/errors, no GIF references |
| Link check, strict mode | Passed, 0 warnings/errors |

The strict builds used `-W --keep-going`, so any Sphinx warning would have made the command fail.

## Reproduction

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r docs\requirements.txt
.\.venv\Scripts\sphinx-intl build -l en -d source\locale
.\.venv\Scripts\sphinx-build -W --keep-going -b html source build\html\zh
.\.venv\Scripts\sphinx-build -W --keep-going -b html -D language=en source build\html\en
.\.venv\Scripts\sphinx-build -W --keep-going -b latex source build\latex
.\.venv\Scripts\sphinx-build -W --keep-going -b linkcheck source build\linkcheck
.\.venv\Scripts\python tools\validate_repository.py
```

## Explicit limits

- XeLaTeX was unavailable on both the Windows host and WSL, so Sphinx's LaTeX source was verified but a final PDF binary was not produced.
- No physical module or firmware image was available. AT commands and hardware procedures were not executed.
- Link checking includes narrowly documented ignores in `source/conf.py` for three generated landing-card HTML paths and the hardware pin label `RX:PA0`; all other checked links passed.

The detailed command record is in `validation-logs/Sphinx-validation.log`.
