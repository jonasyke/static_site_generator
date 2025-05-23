from block_markdown import markdown_to_blocks
import unittest

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_markdown_to_blocks_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_no_paragraphs(self):
        md = "This is a single line of text."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single line of text."])

    def test_markdown_to_blocks_multiple_paragraphs(self):
        md = "This is the first paragraph.\n\nThis is the second paragraph."
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first paragraph.",
                "This is the second paragraph.",
            ],
        )
    def test_markdown_to_blocks_with_extra_newlines(self):
        md = "This is the first paragraph.\n\n\nThis is the second paragraph."
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first paragraph.",
                "This is the second paragraph.",
            ],
        )

if __name__ == "__main__":
    unittest.main()