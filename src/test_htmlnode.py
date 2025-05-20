import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    
    def test_init(self):
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'greeting'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello, World!')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {'class': 'greeting'})
    
    def test_to_html(self):
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'greeting'})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_props_to_html(self):
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'greeting', 'id': None})
        self.assertEqual(node.props_to_html(), 'class="greeting"')
    
    def test_repr(self):
        node = HTMLNode(tag='div', value='Hello, World!', children=[], props={'class': 'greeting'})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, World!, [], {'class': 'greeting'})")
    
    def test_repr_empty(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode(None, None, None, None)")
    
    def test_repr_no_props(self):
        node = HTMLNode(tag='div', value='Hello, World!', children=[])
        self.assertEqual(repr(node), "HTMLNode(div, Hello, World!, [], None)")
    
    def test_repr_no_children(self):
        node = HTMLNode(tag='div', value='Hello, World!', props={'class': 'greeting'})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, World!, None, {'class': 'greeting'})")
    
    def test_repr_no_value(self):
        node = HTMLNode(tag='div', children=[], props={'class': 'greeting'})
        self.assertEqual(repr(node), "HTMLNode(div, None, [], {'class': 'greeting'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
def test_leaf_to_html_img(self):
    with self.assertRaises(ValueError):
        node = LeafNode("img", None, {"src": "image.png"})

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    


    

if __name__ == "__main__":
    unittest.main()
