import unittest
from utils import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_h1(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_h1_with_whitespace(self):
        markdown = "#   Spaced Title  "
        self.assertEqual(extract_title(markdown), "Spaced Title")

    def test_no_h1(self):
        markdown = "## Subheader\nText"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_empty_markdown(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_multiple_lines(self):
        markdown = "Some text\n# Title\nMore text"
        self.assertEqual(extract_title(markdown), "Title")



if __name__ == '__main__':
    unittest.main()