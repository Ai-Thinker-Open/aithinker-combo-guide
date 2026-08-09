[![中文](https://img.shields.io/badge/中文-README-blue)](USAGE.zh.md)

# Combo-AT Guide maintainer handbook

This handbook is for maintainers who are new to Sphinx, gettext, or Read the Docs. It explains the repository layout, the bilingual publishing model, safe editing, local verification, and release troubleshooting.

## Contents

1. [Purpose](#1-purpose)
2. [Core concepts](#2-core-concepts)
3. [Repository structure](#3-repository-structure)
4. [Navigation and content groups](#4-navigation-and-content-groups)
5. [Writing reStructuredText](#5-writing-restructuredtext)
6. [Editing workflow](#6-editing-workflow)
7. [Maintaining English translations](#7-maintaining-english-translations)
8. [Local setup and validation](#8-local-setup-and-validation)
9. [Read the Docs deployment](#9-read-the-docs-deployment)
10. [Troubleshooting](#10-troubleshooting)
11. [Glossary](#11-glossary)

## 1. Purpose

The repository is the source for the Ai-Thinker Combo-AT documentation. It provides:

- firmware and hardware introduction;
- a reference for the supported AT command groups;
- provisioning, OTA, networking, cloud, and Bluetooth examples;
- Chinese and English sites generated from one source tree.

The main site entry is `source/index.rst`. It links to getting-started documents, the command reference, and command examples.

## 2. Core concepts

### 2.1 Source and translated languages

Chinese `.rst` files are authoritative. English is not maintained as a second `.rst` tree. Sphinx extracts Chinese messages into `.pot` templates, and maintainers translate them in `.po` catalogs.

```text
Chinese .rst
  -> Sphinx gettext builder
  -> .pot templates
  -> sphinx-intl update
  -> English msgstr entries in .po
  -> sphinx-intl build
  -> .mo catalogs
  -> English Sphinx output
```

### 2.2 reStructuredText

reStructuredText is the primary source format. Common constructs are:

```rst
Section title
=============

``inline code``

**bold text**

`external link <https://example.com>`__

.. code-block:: none

   AT+GMR
```

Use anonymous external links (`__`) when a page repeats the same visible link label. Named links (`_`) create explicit targets and duplicate labels cause warnings.

### 2.3 PO and MO files

| File | Maintained by | Purpose |
| --- | --- | --- |
| `.po` | humans and `sphinx-intl update` | editable message catalog |
| `.mo` | `sphinx-intl build` | compiled catalog read by gettext |

Do not edit `msgid` manually. It represents the extracted source text. Translate `msgstr`, preserve markup, review fuzzy entries, then compile the catalogs.

### 2.4 One configuration, two languages

`source/conf.py` reads `READTHEDOCS_LANGUAGE`. Without the variable it defaults to `zh_CN`; the English Read the Docs project supplies `en`. Locally, `-D language=en` provides the same override.

### 2.5 Read the Docs model

The intended deployment is one Git repository imported as two Read the Docs projects:

- Chinese main project: `Simplified Chinese (zh_CN)`;
- English translation project: `English (en)`.

Associate the English project under the main project's Translations settings so the hosted site exposes a language selector.

## 3. Repository structure

```text
aithinker-combo-guide/
  source/
    conf.py
    index.rst
    docs/
      instruction/
      command-set/
      command-examples/
    _static/
    locale/en/LC_MESSAGES/
  docs/requirements.txt
  .readthedocs.yaml
  Makefile
  make.bat
  README.md
  README.zh.md
  USAGE.md
  USAGE.zh.md
```

There are 26 Chinese `.rst` documents and 26 matching English `.po` catalogs. Each catalog should compile to one `.mo` file.

Build output belongs under `build/` and is ignored by Git. Do not commit virtual environments or Read the Docs credentials.

## 4. Navigation and content groups

### 4.1 Getting started

`source/docs/instruction/` contains the Combo-AT introduction, hardware connection, firmware download, firmware differences, and error-code documents.

### 4.2 Command reference

`source/docs/command-set/` contains Basic, Wi-Fi, TCP/IP, HTTP, MQTT, BLE, SNTP, driver, and Granwin platform command references.

### 4.3 Command examples

`source/docs/command-examples/` covers network provisioning, OTA, TCP/IP, MQTT, HTTP, BLE, Granwin platform, and sleep examples.

Every new page must appear in a parent `toctree`; otherwise it can build without appearing in navigation.

## 5. Writing reStructuredText

### 5.1 Command pages

A command section normally contains an anchor, title, command form, response, parameter list, notes, and an example:

```rst
.. _cmd-EXAMPLE:

AT+EXAMPLE set a value
----------------------

**Command:**

.. code-block:: none

   AT+EXAMPLE=<value>

**Response:**

.. code-block:: none

   OK
```

Keep underline lengths at least as long as their headings. Separate nested lists and literal blocks correctly; strict Sphinx builds reject ambiguous indentation.

### 5.2 Images and PDF compatibility

LaTeX cannot embed animated GIF files. Provide a same-purpose PNG fallback:

```rst
.. only:: format_html

   .. figure:: ../../_static/example.gif

.. only:: format_latex

   .. figure:: ../../_static/example.png
```

### 5.3 Content safety

- Keep command tokens, parameter names, model numbers, URLs, and response strings exact.
- Do not change a command solely to improve wording.
- Do not claim hardware validation without a command transcript and device evidence.
- Use literal markup for protocol terms unless a real Sphinx glossary entry exists.

## 6. Editing workflow

1. Edit the Chinese `.rst` source.
2. Build Chinese HTML with warnings treated as errors.
3. Generate gettext templates.
4. Update the English catalogs.
5. Translate new or changed messages and review fuzzy matches.
6. Compile `.mo` catalogs.
7. Build English HTML with warnings treated as errors.
8. Build LaTeX source and verify that it contains no `.gif` references.
9. Run link checking and review every excluded false positive.

Example commands:

```powershell
sphinx-build -W --keep-going -b html source build\html\zh
sphinx-build -b gettext source build\gettext
sphinx-intl update -p build\gettext -l en -d source\locale
sphinx-intl build -l en -d source\locale
sphinx-build -W --keep-going -b html -D language=en source build\html\en
sphinx-build -W --keep-going -b latex source build\latex
sphinx-build -W --keep-going -b linkcheck source build\linkcheck
```

## 7. Maintaining English translations

### 7.1 What to translate

Translate human-readable headings, descriptions, notes, table cells, and procedure text. Preserve:

- reST roles and directives;
- substitution identifiers and reference targets;
- AT command strings and response tokens;
- URLs, UUIDs, model names, and parameter placeholders.

For example, a translated link may change its visible text but must keep the original internal target.

### 7.2 Coverage checks

Before committing, confirm:

- every current source message has a nonempty `msgstr`;
- there are no fuzzy messages left unreviewed;
- every `.po` parses without a BOM warning;
- the number of `.rst`, `.po`, and compiled `.mo` catalogs matches;
- the strict English build reports zero warnings.

### 7.3 New pages

For a new `.rst` page:

1. add it to the parent `toctree`;
2. run the gettext and `sphinx-intl update` commands;
3. translate the new `.po` catalog completely;
4. compile and build both languages;
5. verify all images and internal links.

## 8. Local setup and validation

### 8.1 Create an environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r docs\requirements.txt
```

Use the pinned file. Sphinx 4.5 is incompatible with the latest major `sphinxcontrib-*` releases.

### 8.2 Build output

| Output | Command | Entry |
| --- | --- | --- |
| Chinese HTML | `sphinx-build -b html source build/html/zh` | `build/html/zh/index.html` |
| English HTML | `sphinx-build -b html -D language=en source build/html/en` | `build/html/en/index.html` |
| LaTeX source | `sphinx-build -b latex source build/latex` | generated `.tex` file |
| Link report | `sphinx-build -b linkcheck source build/linkcheck` | `output.txt` |

Always add `-W --keep-going` for review builds so warnings fail the command while reporting all detected issues.

### 8.3 Final PDF

The Sphinx LaTeX builder only creates `.tex` and copied assets. Producing a PDF requires XeLaTeX, xeCJK, compatible CJK fonts, and the remaining LaTeX packages. Do not report a PDF as validated when only `.tex` was generated.

## 9. Read the Docs deployment

`.readthedocs.yaml` selects Ubuntu 22.04, Python 3.8, all output formats, `source/conf.py`, and `docs/requirements.txt`. Its pre-build job compiles English catalogs before Sphinx runs.

Normal publication is:

```text
reviewed commit
  -> GitHub push or merge
  -> Read the Docs webhook
  -> dependency installation
  -> sphinx-intl catalog compilation
  -> Sphinx build
  -> hosted Chinese and English projects
```

Check the Read the Docs build log after dependency or configuration changes. A local success on a different Python version is useful evidence but does not replace the hosted build result.

## 10. Troubleshooting

### English pages show Chinese

- Ensure the project language is `en` or pass `-D language=en`.
- Confirm each relevant `msgstr` is nonempty and not fuzzy.
- Compile `.po` to `.mo` before building.

### Sphinx refuses a `sphinxcontrib` extension

Recreate the environment from `docs/requirements.txt`. Do not upgrade the extensions independently while the project remains on Sphinx 4.5.

### Duplicate explicit target

Repeated named external links share a generated target. Change repeated external links to the anonymous form ending in `__`.

### Title underline too short

Extend the reST underline so it is at least as long as the heading.

### PDF contains or rejects GIF

Add a PNG fallback, separate HTML and LaTeX image directives, rebuild LaTeX, and search the generated `.tex` for `.gif`.

### Linkcheck reports a generated HTML path

The site landing page intentionally links image cards to generated `.html` output. `source/conf.py` documents the narrow ignore patterns for these build-time paths and the `RX:PA0` hardware-pin notation. Do not broaden the ignore list to hide real HTTP failures.

## 11. Glossary

| Term | Meaning |
| --- | --- |
| Sphinx | documentation generator used by this repository |
| reST / RST | reStructuredText source format |
| gettext | message extraction and translation system |
| POT | generated source-message template |
| PO | editable translation catalog |
| MO | compiled translation catalog |
| msgid | source-language message key |
| msgstr | translated message |
| fuzzy | translation requiring manual review |
| toctree | Sphinx navigation tree |
| RTD | Read the Docs hosting and build service |
| XeLaTeX | LaTeX engine configured for the final PDF |
