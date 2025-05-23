import unittest

from textnode import TextNode, TextType, extract_markdown_links, extract_markdown_images, text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_TextNode(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertIsNone(node.url)

    def test_TextNodeNotEqual(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
    
    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a text node, link, https://www.boot.dev)")
    
    def test_repr_with_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev/image.png")
        self.assertEqual(repr(node), "TextNode(This is a text node, image, https://www.boot.dev/image.png)")
    
    def test_repr_negative(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(repr(node), "TextNode(This is a text node, italic, None)")

    def test_extract_markdown_links(self):
        text = "[Boot.dev](https://www.boot.dev)"
        expected = [("Boot.dev", "https://www.boot.dev")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links_no_match(self):
        text = "No links here!"
        expected = []
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_match(self):
        matches = extract_markdown_images("This is text with no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_empty_string(self):
        matches = extract_markdown_images("")
        self.assertListEqual([], matches)

    def test_text_to_textnodes(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)

    def test_text_to_textnodes_no_links(self):
        text = "This is just normal text with no formatting."
        expected_nodes = [
            TextNode("This is just normal text with no formatting.", TextType.TEXT)
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)
    
    """def test_text_to_textnodes_empty_string(self):
        text = ""
        expected_nodes = [
            TextNode("", TextType.TEXT)
        ]
        result_nodes = text_to_textnodes(text)
        self.assertEqual(result_nodes, expected_nodes)"""
    



    
    

if __name__ == "__main__":
    unittest.main()