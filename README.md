[![中文](https://img.shields.io/badge/中文-README-blue)](README.zh.md)

# Combo-AT Guide

## Project overview

This repository contains the official Ai-Thinker Combo-AT documentation site. It is a Sphinx project published through Read the Docs and covers firmware introduction, hardware connection, firmware downloads, AT command references, and practical command examples.

Chinese reStructuredText files under `source/docs/` are the source language. English pages are generated from the matching gettext catalogs under `source/locale/en/LC_MESSAGES/`. Both languages are built from the same document tree and configuration.

## Documentation scope

- Getting started, supported modules, hardware connections, firmware downloads, and error codes.
- Basic, Wi-Fi, TCP/IP, HTTP, MQTT, BLE, SNTP, driver, and Granwin platform AT commands.
- Provisioning, OTA, networking, MQTT, HTTP, BLE, cloud-platform, and sleep-mode examples.
- HTML, translated HTML, LaTeX/PDF source, EPUB, and HTML ZIP outputs through Sphinx and Read the Docs.

## Build requirements

- Python 3.8 or later. Read the Docs currently targets Python 3.8.
- The pinned packages in `docs/requirements.txt`.
- XeLaTeX with CJK support only when producing the final PDF locally.

Create an isolated environment and install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r docs\requirements.txt
```

The repository pins the Sphinx 4.5-compatible `sphinxcontrib-*` releases. Installing current 2.x extension releases with Sphinx 4.5 causes the build to stop before reading the documents.

## Usage: build and preview

Compile the English catalogs, then build both sites:

```powershell
sphinx-intl build -l en -d source\locale
sphinx-build -W --keep-going -b html source build\html\zh
sphinx-build -W --keep-going -b html -D language=en source build\html\en
```

Open these files in a browser:

- Chinese: `build/html/zh/index.html`
- English: `build/html/en/index.html`

Generate LaTeX source and check that animated GIF files are not passed to the PDF toolchain:

```powershell
sphinx-build -W --keep-going -b latex source build\latex
Select-String -Path build\latex\*.tex -Pattern "\.gif"
```

The final command should produce no matches. A complete PDF additionally requires XeLaTeX and the configured CJK fonts.

## Repository structure

```text
source/
  conf.py                         Sphinx, language, theme, and PDF configuration
  index.rst                       site entry and top-level navigation
  docs/instruction/              introduction, hardware, firmware, and errors
  docs/command-set/              AT command reference
  docs/command-examples/         scenario-based command examples
  _static/                        images, animations, and CSS
  locale/en/LC_MESSAGES/         English .po sources and compiled .mo catalogs
docs/requirements.txt            reproducible documentation dependencies
.readthedocs.yaml                Read the Docs build configuration
README.md / README.zh.md         repository overview
USAGE.md / USAGE.zh.md           maintainer handbook
```

## Translation workflow

After changing Chinese `.rst` content:

```powershell
sphinx-build -b gettext source build\gettext
sphinx-intl update -p build\gettext -l en -d source\locale
# Translate every new msgstr and clear only translations that were reviewed.
sphinx-intl build -l en -d source\locale
sphinx-build -W --keep-going -b html -D language=en source build\html\en
```

Do not translate substitution identifiers, reference targets, AT commands, URLs, model names, or reST syntax. Translate only the visible text. An empty or fuzzy `msgstr` means the English site is incomplete.

## Verified maintenance flow

```text
source/index.rst
  -> three section indexes
  -> Chinese .rst pages
  -> gettext catalogs (.po)
  -> compiled translations (.mo)
  -> Chinese/English Sphinx builders
  -> HTML and LaTeX/PDF source
  -> Read the Docs deployment
```

Detailed evidence:

- [Code entry](docs/CODE_ENTRY.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Validation](docs/VALIDATION.md)
- [Maintainer handbook](USAGE.md)

## Validation status

The recorded review installs the requirements in a clean Python 3.12 environment, compiles all 26 English catalogs, verifies that all 1,425 current source messages have non-empty, non-fuzzy English translations, and builds 28 Chinese plus 28 English HTML pages with warnings treated as errors. LaTeX source and external link checking also pass without warnings.

The validation machine has no XeLaTeX installation, so a final PDF binary was not generated. See the validation report for the exact commands, environment, and limits.

## Troubleshooting

- **Sphinx 4.5 rejects a `sphinxcontrib` extension:** install only from the pinned requirements file.
- **English pages contain Chinese:** update the `.po` files, remove fuzzy markers after review, and run `sphinx-intl build` before the English build.
- **Duplicate explicit target warning:** use anonymous external links ending in double underscores when the same visible label appears more than once.
- **PDF build fails on GIF:** provide a PNG fallback and use `only:: format_html` / `only:: format_latex` branches.
- **A page is missing from navigation:** include it in the appropriate `toctree`.

## Contribution boundary

Documentation builds validate syntax, references, translations, and output generation. They do not prove that every AT command, firmware download, phone application, cloud service, module variant, or hardware procedure works on a physical device. Changes to commands or parameters should cite the tested module, firmware version, serial settings, command transcript, and observed result.

Do not commit credentials, private cloud identifiers, device secrets, customer data, or local virtual environments.

## License

This repository includes the GNU General Public License version 2. See [LICENSE](LICENSE).
