"""Regression tests for the documentation checker; all data is synthetic."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_docs import anchors, check


class DocumentationTests(unittest.TestCase):
    def validate(self, files):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return check(root)[1]

    def test_valid_links_and_unicode(self):
        self.assertEqual(self.validate({
            "README.md": "# Início\n[local](#início)\n[guia](docs/guia.md#visão)\n",
            "docs/guia.md": "# Visão\n[voltar](../README.md)\n",
        }), [])

    def test_missing_file(self):
        self.assertIn("destino inexistente", self.validate({"README.md": "[x](missing.md)"})[0])

    def test_missing_anchor(self):
        self.assertIn("âncora", self.validate({"README.md": "# Título\n[x](#ausente)"})[0])

    def test_duplicate_headings(self):
        self.assertEqual(anchors("# Teste\n## Teste\n## Teste"), {"teste", "teste-1", "teste-2"})

    def test_directory_fragment(self):
        self.assertEqual(self.validate({
            "README.md": "[docs](docs#guia)", "docs/README.md": "# Guia",
        }), [])

    def test_badge_destination_is_checked(self):
        errors = self.validate({"README.md": "[![badge](https://example.com/b.svg)](missing.md)"})
        self.assertEqual(len(errors), 1)
        self.assertIn("destino inexistente", errors[0])

    def test_external_links_are_not_requested(self):
        self.assertEqual(self.validate({"README.md": "[x](https://example.invalid)\n[m](mailto:a@example.invalid)"}), [])

    def test_fenced_examples_are_ignored(self):
        self.assertEqual(self.validate({"README.md": "```text\n[x](missing.md)\n```\n"}), [])

    def test_unclosed_fence(self):
        self.assertIn("não fechado", self.validate({"README.md": "~~~text\nexemplo"})[0])

    def test_repository_escape(self):
        self.assertIn("fora do repositório", self.validate({"README.md": "[x](../outside.md)"})[0])

    def test_encoded_path(self):
        self.assertEqual(self.validate({"README.md": "[x](guia%20local.md)", "guia local.md": "# Guia"}), [])

    def test_fragment_on_unknown_document(self):
        self.assertIn("âncora", self.validate({"README.md": "[x](LICENSE#termos)", "LICENSE": "texto"})[0])


if __name__ == "__main__":
    unittest.main()
