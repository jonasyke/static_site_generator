import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

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
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "http://example.com"})


    


    

if __name__ == "__main__":
    unittest.main()
