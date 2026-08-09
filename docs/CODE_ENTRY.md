[![中文](https://img.shields.io/badge/中文-文档-blue)](CODE_ENTRY.zh.md)

# Code and documentation entry points

This repository is a documentation project rather than a firmware SDK. Its runtime output is a Sphinx-generated documentation site, so the entry points below describe the documentation build and navigation flow.

## Primary entry points

- `source/index.rst` is the Sphinx root document and the first page of the site.
- `source/conf.py` configures the theme, default language, gettext catalogs, link checking, and LaTeX output.
- `.readthedocs.yaml` is the hosted-build entry point. It selects Python 3.8, installs `docs/requirements.txt`, and compiles the English catalogs before Sphinx runs.
- `docs/requirements.txt` contains the reproducible build dependencies.

## Content entry points

The root `toctree` in `source/index.rst` routes readers to three content groups:

1. `source/docs/instruction/index.rst` — introduction, hardware connection, firmware downloads, and error codes.
2. `source/docs/command-set/index.rst` — the AT command reference.
3. `source/docs/command-examples/index.rst` — practical AT command examples.

## Local build entry

From the repository root, install the pinned dependencies, compile the catalogs, and invoke Sphinx:

```powershell
python -m pip install -r docs\requirements.txt
sphinx-intl build -l en -d source\locale
sphinx-build -W --keep-going -b html source build\html\zh
sphinx-build -W --keep-going -b html -D language=en source build\html\en
```

The generated entry pages are `build/html/zh/index.html` and `build/html/en/index.html`.

## Boundary

The repository documents AT firmware behavior but does not contain the firmware implementation or a device test harness. The entry-point review therefore verifies the documentation build and navigation path; it does not claim execution of AT commands on physical hardware.
