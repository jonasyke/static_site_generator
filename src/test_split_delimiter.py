from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
import unittest

class TestSplitDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a test.", TextType.TEXT)
        ]
        delimiter = ", "
        text_type = TextType.TEXT
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        expected_nodes = [
            TextNode("Hello", TextType.TEXT),
            TextNode("world!", TextType.TEXT),
            TextNode("This is a test.", TextType.TEXT)
        ]
        
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_no_split(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.TEXT),
            TextNode("This is a test.", TextType.TEXT)
        ]
        delimiter = " "
        text_type = TextType.TEXT
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        expected_nodes = [
            TextNode("Hello,", TextType.TEXT),
            TextNode("world!", TextType.TEXT),
            TextNode("This", TextType.TEXT),
            TextNode("is", TextType.TEXT),
            TextNode("a", TextType.TEXT),
            TextNode("test.", TextType.TEXT)
        ]
        
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_empty(self):
        old_nodes = []
        delimiter = ", "
        text_type = TextType.TEXT
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        expected_nodes = []
        
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_text_type(self):
        old_nodes = [
            TextNode("Hello, world!", TextType.BOLD),
            TextNode("This is a test.", TextType.TEXT)
        ]
        delimiter = ", "
        text_type = TextType.TEXT
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        expected_nodes = [
            TextNode("Hello, world!", TextType.BOLD),
            TextNode("This is a test.", TextType.TEXT)
        ]
        
        self.assertEqual(new_nodes, expected_nodes)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev/2)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.boot.dev/2"),
            ],
            new_nodes,
        )
    def test_split_links_no_links(self):
        node = TextNode(
            "This is text with no links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no links", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_links_empty_string(self):
        node = TextNode(
            "",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_links_no_text_type(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev/2)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev/2)", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode(
            "This is text with no images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.TEXT),
            ],
            new_nodes,
        )
    
if __name__ == "__main__":
    unittest.main()