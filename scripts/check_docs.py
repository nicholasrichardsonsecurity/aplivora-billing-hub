"""Check this repository's inline Markdown links without network access.

Supported subset: ATX headings, inline links/images and fenced code blocks.
This is a documentation check, not a security scanner or full Markdown parser.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def visible_lines(content):
    """Yield line numbers and text outside fenced code blocks."""
    fence = None
    for number, line in enumerate(content.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            yield number, line
    if fence is not None:
        raise ValueError("bloco de código não fechado")


def anchors(content):
    used = set()
    for _, line in visible_lines(content):
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", line)
        if not heading:
            continue
        text = heading.group(1).lower()
        slug = re.sub(r"[^\w\- ]", "", text).replace(" ", "-")
        candidate = slug
        suffix = 0
        while candidate in used:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        used.add(candidate)
    return used


def check(root):
    root = root.resolve()
    documents = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
    errors = []
    parsed = {}
    for path in documents:
        try:
            content = path.read_text(encoding="utf-8")
            parsed[path] = (list(visible_lines(content)), anchors(content))
        except (UnicodeError, ValueError) as error:
            errors.append(f"{path.relative_to(root)}:1 - {error}")
    for path, (lines, _) in parsed.items():
        for number, line in lines:
            for raw in re.findall(r"\]\(([^\s)]+)\)", line):
                url = urlsplit(raw)
                if url.scheme or url.netloc:
                    continue
                destination = (path.parent / unquote(url.path)).resolve() if url.path else path
                prefix = f"{path.relative_to(root)}:{number}"
                if not destination.is_relative_to(root):
                    errors.append(f"{prefix} - link fora do repositório: {raw}")
                elif not destination.exists():
                    errors.append(f"{prefix} - destino inexistente: {raw}")
                elif url.fragment:
                    if destination.is_dir():
                        destination = destination / "README.md"
                    target = parsed.get(destination)
                    if target is None or unquote(url.fragment) not in target[1]:
                        errors.append(f"{prefix} - âncora não verificada: {raw}")
    return documents, errors


if __name__ == "__main__":
    documents, errors = check(Path(__file__).resolve().parents[1])
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {len(documents)} arquivos Markdown; links locais e blocos verificados.")
