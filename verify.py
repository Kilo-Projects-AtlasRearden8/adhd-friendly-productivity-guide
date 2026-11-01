#!/usr/bin/env python3
"""Verification script for the ADHD-friendly productivity guide.

Checks:
- HTML files parse cleanly (html.parser)
- Internal href/src links resolve to existing files
- No external URLs (local-first, no secrets)
- LICENSE contains the exact required copyright line
- README credits Asdale Dynamics, LLC
- Markdown files exist and link to existing worksheets
"""
import html.parser
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)
    print("ERROR: " + msg)


def warning(msg):
    WARNINGS.append(msg)
    print("WARNING: " + msg)


class LinkChecker(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.base_dir = os.path.dirname(path)
        self.links = []

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr in ("href", "src") and value:
                self.links.append((tag, attr, value))


def check_html(path):
    rel = os.path.relpath(path, ROOT)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse with html.parser to catch structural errors
    parser = HTMLParser()
    try:
        parser.feed(content)
        parser.close()
    except Exception as exc:  # noqa: BLE001 - report parse problems
        error(f"{rel}: HTML parse error: {exc}")
        return

    # Link resolution
    checker = LinkChecker(path)
    checker.feed(content)
    for tag, attr, value in checker.links:
        parsed = urlparse(value)
        if parsed.scheme in ("http", "https"):
            error(f"{rel}: external URL in {tag} {attr}: {value}")
            continue
        if parsed.scheme not in ("", "mailto", "tel"):
            continue
        target = os.path.normpath(os.path.join(checker.base_dir, parsed.path))
        if not os.path.exists(target):
            error(f"{rel}: broken link {tag}={value} -> {target} (not found)")


def check_file_text(path, patterns, label, must=True):
    rel = os.path.relpath(path, ROOT)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for pat in patterns:
        found = re.search(pat, content)
        if must and not found:
            error(f"{rel}: missing expected {label}: {pat}")
        elif not must and found:
            warning(f"{rel}: unexpected {label} found: {pat}")


def main():
    html_files = []
    for dirpath, _dirs, files in os.walk(ROOT):
        # skip .git
        if ".git" in dirpath.split(os.sep):
            continue
        for name in files:
            full = os.path.join(dirpath, name)
            if name.endswith(".html"):
                html_files.append(full)
            elif name.endswith(".md"):
                check_file_text(full, [], "", must=False)  # placeholder

    for path in sorted(html_files):
        check_html(path)

    # LICENSE
    lic = os.path.join(ROOT, "LICENSE")
    with open(lic, "r", encoding="utf-8") as f:
        lic_content = f.read()
    if "Copyright (c) 2026 Asdale Dynamics, LLC" not in lic_content:
        error("LICENSE: missing exact line 'Copyright (c) 2026 Asdale Dynamics, LLC'")

    # README credits
    readme = os.path.join(ROOT, "README.md")
    with open(readme, "r", encoding="utf-8") as f:
        readme_content = f.read()
    if "Asdale Dynamics, LLC" not in readme_content:
        error("README.md: does not credit Asdale Dynamics, LLC")

    # No obvious secrets
    secret_patterns = [r"sk-[A-Za-z0-9]{20,}", r"AKIA[0-9A-Z]{16}", r"password\s*=\s*.+", r"api[_-]?key\s*=\s*.+"]
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        for name in files:
            full = os.path.join(dirpath, name)
            if name == ".git" or name.endswith((".png", ".jpg", ".pdf", ".zip")):
                continue
            try:
                with open(full, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
            for pat in secret_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    warning(f"{os.path.relpath(full, ROOT)}: possible secret pattern: {pat}")

    # Docs -> worksheets links
    docs_dir = os.path.join(ROOT, "docs")
    ws_dir = os.path.join(ROOT, "worksheets")
    for md in ["tiny-tasks.md", "body-doubling.md", "energy-friendly-routines.md", "printable-worksheets.md"]:
        path = os.path.join(docs_dir, md)
        if not os.path.exists(path):
            error(f"missing docs file: {md}")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for m in re.finditer(r"\((\.\./worksheets/[^)]+)\)", content):
            target = os.path.normpath(os.path.join(os.path.dirname(path), m.group(1)))
            if not os.path.exists(target):
                error(f"{md}: links to missing worksheet {m.group(1)}")

    print("\n--- Results ---")
    print("HTML files checked: %d" % len(html_files))
    print("Errors: %d" % len(ERRORS))
    print("Warnings: %d" % len(WARNINGS))
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
