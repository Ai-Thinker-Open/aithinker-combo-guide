[![中文](https://img.shields.io/badge/中文-文档-blue)](ARCHITECTURE.zh.md)

# Architecture

## Overview

The project uses one reStructuredText source tree and gettext catalogs to publish Chinese and English versions of the same Sphinx site.

```text
.readthedocs.yaml
        |
        +--> docs/requirements.txt
        |
        +--> sphinx-intl --> source/locale/en/LC_MESSAGES/*.po --> *.mo
        |
        +--> source/conf.py + source/index.rst
                           |
                           +--> instruction
                           +--> command-set
                           +--> command-examples
                           |
                           +--> Chinese/English HTML, LaTeX, EPUB, HTML ZIP
```

## Components and responsibilities

- `source/index.rst` owns the top-level navigation.
- `source/docs/` owns the Chinese source content, split into instruction, command reference, and examples.
- `source/locale/en/LC_MESSAGES/` owns the English gettext catalogs. Each source `.rst` has a matching `.po` and compiled `.mo` file.
- `source/_static/` and images stored beside documents provide the referenced visual assets.
- `source/conf.py` selects `zh_CN` by default and accepts `READTHEDOCS_LANGUAGE` or `-D language=en` for the English build.
- `.readthedocs.yaml` connects the repository to the hosted build service and requests all supported output formats.

## Translation flow

1. A maintainer edits the Chinese `.rst` source.
2. Sphinx extracts translatable messages to gettext templates.
3. `sphinx-intl` updates the English `.po` files.
4. Translators complete the `msgstr` values.
5. `sphinx-intl build` compiles `.po` to `.mo`.
6. Sphinx reads the same document tree with `language=en` to render the English site.

## Dependency design

Sphinx is pinned to 4.5 for compatibility with the hosted Python 3.8 build. The `sphinxcontrib-*` packages are also explicitly pinned to their Sphinx 4-compatible releases. This prevents a clean installation from selecting newer extensions that require Sphinx 5 or later.

## Maintenance constraints

- Keep `.rst`, `.po`, and `.mo` paths aligned.
- Build both languages with warnings treated as errors after changing navigation, links, substitutions, or translations.
- Do not treat successful documentation rendering as proof that commands work on a specific firmware or hardware revision.
