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


    