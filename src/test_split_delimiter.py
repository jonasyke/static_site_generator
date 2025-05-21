from split_delimiter import split_nodes_delimiter
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

if __name__ == "__main__":
    unittest.main()