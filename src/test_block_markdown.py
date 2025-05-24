from block_markdown import markdown_to_blocks, block_to_block_type
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
    def test_markdown_to_blocks_with_leading_trailing_spaces(self):
        md = "   This is the first paragraph.   \n\n   This is the second paragraph.   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first paragraph.",
                "This is the second paragraph.",
            ],
        )
    def test_markdown_to_blocks_with_special_characters(self):
        md = "This is a paragraph with special characters: !@#$%^&*()"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph with special characters: !@#$%^&*()",
            ],
        )
    def test_markdown_to_blocks_with_code_block(self):
        md = """
        This is a paragraph.

        ```
        def hello_world():
            print("Hello, world!")
        ```
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph.",
                "```\n        def hello_world():\n            print(\"Hello, world!\")\n        ```",
            ],
        )
    def test_block_to_block_type(self):
        block = "This is a paragraph."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "paragraph")

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "heading")

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "quote")

    def test_block_to_block_type_unordered_list(self):
        block = "- This is an unordered list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "unordered_list")

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is an ordered list item"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "ordered_list")

    def test_block_to_block_type_code(self):
        block = "```\nprint('Hello, world!')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "code")

    def test_block_to_block_type_multiple_lines(self):
        block = "This is a paragraph.\nThis is another line."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "paragraph")

    def test_block_to_block_type_multiple_lines_quote(self):
        block = "> This is a quote.\n> This is another line of the quote."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "quote")

    def test_block_to_block_type_multiple_lines_unordered_list(self):
        block = "- This is an unordered list item.\n- This is another item."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "unordered_list")

    def test_block_to_block_type_multiple_lines_ordered_list(self):
        block = "1. This is an ordered list item.\n2. This is another item."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "ordered_list")

    def test_block_to_block_type_multiple_lines_code(self):
        block = "```\nprint('Hello, world!')\nprint('Another line')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "code")

    def test_block_to_block_type_empty_string(self):
        block = ""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "paragraph")

    def test_block_to_block_type_only_newlines(self):
        block = "\n\n"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "paragraph")

    def test_block_to_block_type_only_spaces(self):
        block = "   "
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, "paragraph")

    
    

if __name__ == "__main__":
    unittest.main()