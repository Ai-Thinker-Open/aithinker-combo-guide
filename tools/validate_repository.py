#!/usr/bin/env python3
"""Run fast structural checks for the bilingual Sphinx repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from babel.messages.pofile import read_po


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
CATALOG_ROOT = SOURCE / "locale" / "en" / "LC_MESSAGES"
IMAGE_DIRECTIVE = re.compile(
    r"^\s*\.\.\s+(?:\|[^|]+\|\s+)?(?:image|figure)::\s+(\S+)", re.MULTILINE
)
REQUIRED_PINS = {
    "Sphinx": "4.5.0",
    "sphinxcontrib-applehelp": "1.0.4",
    "sphinxcontrib-devhelp": "1.0.2",
    "sphinxcontrib-htmlhelp": "2.0.0",
    "sphinxcontrib-qthelp": "1.0.3",
    "sphinxcontrib-serializinghtml": "1.1.5",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_markdown_pairs(errors: list[str]) -> tuple[int, int]:
    files = sorted(ROOT.rglob("*.md"))
    files = [path for path in files if "validation-logs" not in path.parts]
    for path in files:
        if path.name.endswith(".zh.md"):
            peer = path.with_name(path.name.removesuffix(".zh.md") + ".md")
            required_target = peer.name
            badge_language = "English"
        else:
            peer = path.with_name(path.stem + ".zh.md")
            required_target = peer.name
            badge_language = "中文"
        if not peer.is_file():
            fail(errors, f"missing Markdown language peer: {path.relative_to(ROOT)}")
            continue
        first_line = path.read_text(encoding="utf-8-sig").splitlines()[0]
        if badge_language not in first_line or f"]({required_target})" not in first_line:
            fail(errors, f"invalid language badge: {path.relative_to(ROOT)}")
    return len(files), len(files) // 2


def check_catalogs(errors: list[str]) -> tuple[int, int, int, int, int, int, int]:
    rst_files = sorted(SOURCE.rglob("*.rst"))
    po_files = sorted(CATALOG_ROOT.rglob("*.po"))
    mo_files = sorted(CATALOG_ROOT.rglob("*.mo"))
    expected_po = {
        CATALOG_ROOT / path.relative_to(SOURCE).with_suffix(".po") for path in rst_files
    }
    expected_mo = {path.with_suffix(".mo") for path in expected_po}
    actual_po, actual_mo = set(po_files), set(mo_files)
    for path in sorted(expected_po - actual_po):
        fail(errors, f"missing PO catalog: {path.relative_to(ROOT)}")
    for path in sorted(actual_po - expected_po):
        fail(errors, f"orphan PO catalog: {path.relative_to(ROOT)}")
    for path in sorted(expected_mo - actual_mo):
        fail(errors, f"missing MO catalog: {path.relative_to(ROOT)}")
    for path in sorted(actual_mo - expected_mo):
        fail(errors, f"orphan MO catalog: {path.relative_to(ROOT)}")

    total = untranslated = fuzzy = bom = 0
    for path in po_files:
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            bom += 1
            fail(errors, f"UTF-8 BOM in catalog: {path.relative_to(ROOT)}")
        with path.open("r", encoding="utf-8") as handle:
            catalog = read_po(handle, locale="en")
        for message in catalog:
            if not message.id:
                continue
            total += 1
            if "fuzzy" in message.flags:
                fuzzy += 1
            strings = message.string if isinstance(message.string, tuple) else (message.string,)
            if not strings or any(not value for value in strings):
                untranslated += 1
    if untranslated:
        fail(errors, f"untranslated current messages: {untranslated}")
    if fuzzy:
        fail(errors, f"fuzzy current messages: {fuzzy}")
    return len(rst_files), len(po_files), len(mo_files), total, untranslated, fuzzy, bom


def check_local_images(errors: list[str]) -> int:
    checked = 0
    for rst in sorted(SOURCE.rglob("*.rst")):
        text = rst.read_text(encoding="utf-8-sig")
        for value in IMAGE_DIRECTIVE.findall(text):
            if "://" in value or value.startswith("data:") or "*" in value:
                continue
            checked += 1
            target = (rst.parent / value).resolve()
            if not target.is_file():
                fail(
                    errors,
                    f"missing image referenced by {rst.relative_to(ROOT)}: {value}",
                )
    return checked


def check_pins(errors: list[str]) -> int:
    requirements = (ROOT / "docs" / "requirements.txt").read_text(
        encoding="utf-8-sig"
    )
    found = {}
    for line in requirements.splitlines():
        if "==" in line and not line.lstrip().startswith("#"):
            name, version = line.split("==", 1)
            found[name.strip().lower()] = version.strip()
    for name, version in REQUIRED_PINS.items():
        if found.get(name.lower()) != version:
            fail(errors, f"required dependency pin missing: {name}=={version}")
    return len(REQUIRED_PINS)


def main() -> int:
    errors: list[str] = []
    markdown_files, markdown_pairs = check_markdown_pairs(errors)
    rst_count, po_count, mo_count, messages, untranslated, fuzzy, bom = check_catalogs(errors)
    image_count = check_local_images(errors)
    pin_count = check_pins(errors)

    print(f"Markdown: {markdown_files} files / {markdown_pairs} bilingual pairs")
    print(f"Sphinx sources: {rst_count} RST / {po_count} PO / {mo_count} MO")
    print(
        f"English messages: {messages} current / {untranslated} untranslated / "
        f"{fuzzy} fuzzy / {bom} BOM"
    )
    print(f"Local image references checked: {image_count}")
    print(f"Required dependency pins checked: {pin_count}")
    if errors:
        print("FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository structural validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
