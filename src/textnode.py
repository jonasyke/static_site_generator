from enum import Enum
import re

class TextType(Enum):
    TEXT = "Normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def extract_markdown_images(text):
    """
     takes raw markdown text and returns a list of tuples. Each tuple should contain the alt text and the URL of any markdown images.
    """
    image_pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(image_pattern, text)
    return [(alt_text, url) for alt_text, url in matches]

def extract_markdown_links(text):
    """
         extracts markdown links instead of images. It should return tuples of anchor text and URLs.
    """
    link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(link_pattern, text)
    return [(anchor_text, url) for anchor_text, url in matches]

def text_to_textnodes(text):
    """ converts a raw string of markdown-flavored text into a list of TextNode objects.
        it should take a string like this:
        This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
        
       """
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")

    # Split the text into parts based on the delimiters
    parts = re.split(r"(\*\*.*?\*\*|__.*?__|_.*?_|\*\*.*?\*\*|`.*?`|!\[.*?\]\(.*?\)|\[.*?\]\(.*?\))", text)
    
    # Create a list to hold the TextNode objects
    nodes = []

    for part in parts:
        if not part.strip():
            continue

        if part.startswith("![") and part.endswith(")"):
            alt_text, url = extract_markdown_images(part)[0]
            nodes.append(TextNode(alt_text, TextType.IMAGE, url))
        elif part.startswith("[") and part.endswith(")"):
            anchor_text, url = extract_markdown_links(part)[0]
            nodes.append(TextNode(anchor_text, TextType.LINK, url))
        elif part.startswith("**") and part.endswith("**"):
            nodes.append(TextNode(part[2:-2], TextType.BOLD))
        elif part.startswith("__") and part.endswith("__"):
            nodes.append(TextNode(part[2:-2], TextType.BOLD))
        elif part.startswith("_") and part.endswith("_"):
            nodes.append(TextNode(part[1:-1], TextType.ITALIC))
        elif part.startswith("`") and part.endswith("`"):
            nodes.append(TextNode(part[1:-1], TextType.CODE))
        else:
            nodes.append(TextNode(part, TextType.TEXT))

    return nodes

