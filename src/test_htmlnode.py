import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_with_no_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    


    

if __name__ == "__main__":
    unittest.main()
