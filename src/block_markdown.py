from enum import Enum
import re
from textnode import TextNode, TextType, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'
    CODE = 'code'

def markdown_to_blocks(markdown):
    # Split on double newlines, handling code blocks carefully
    blocks = []
    current_block = []
    in_code_block = False

    # Normalize input by removing leading/trailing whitespace
    markdown = markdown.strip()
    if not markdown:
        return []

    for line in markdown.split('\n'):
        stripped_line = line.strip()
        if stripped_line.startswith('```'):
            in_code_block = not in_code_block
            current_block.append(line)
            if not in_code_block:
                blocks.append('\n'.join(current_block).strip())
                current_block = []
            continue
        if in_code_block:
            current_block.append(line)
        elif stripped_line or current_block:
            if not stripped_line and current_block:
                blocks.append('\n'.join(current_block).strip())
                current_block = []
            else:
                current_block.append(line)
    
    if current_block:
        blocks.append('\n'.join(current_block).strip())
    
    return [block for block in blocks if block]

def block_to_block_type(block):
    if not block.strip():
        return BlockType.PARAGRAPH

    lines = block.split('\n')
    first_line = lines[0].strip()

    # Handle code blocks (fenced with ```)
    if first_line.startswith('```') and (len(lines) == 1 or lines[-1].strip().startswith('```')):
        return BlockType.CODE

    # Handle headings (1 to 6 # symbols followed by space)
    if re.match(r'^#{1,6}\s+', first_line):
        return BlockType.HEADING

    # Handle quotes (all non-empty lines start with >)
    if all(line.strip().startswith('>') or not line.strip() for line in lines):
        return BlockType.QUOTE

    # Handle unordered lists (at least one line starts with - or *)
    if any(re.match(r'^[-*]\s+', line.strip()) for line in lines if line.strip()):
        return BlockType.UNORDERED_LIST

    # Handle ordered lists (at least one line starts with number followed by .)
    if any(re.match(r'^\d+\.\s+', line.strip()) for line in lines if line.strip()):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        lines = block.split('\n')

        if block_type == BlockType.PARAGRAPH:
            # Join non-empty lines with a single space, parse inline Markdown
            text = ' '.join(line.strip() for line in lines if line.strip())
            if text:
                text_nodes = text_to_textnodes(text)
                paragraph_children = [text_node_to_html_node(text_node) for text_node in text_nodes]
                children.append(ParentNode(tag='p', children=paragraph_children))

        elif block_type == BlockType.HEADING:
            # Extract heading level and text, parse inline Markdown
            level = len(re.match(r'^(#{1,6})\s+', block).group(1))
            text = re.sub(r'^#{1,6}\s+', '', block).strip()
            if text:
                text_nodes = text_to_textnodes(text)
                heading_children = [text_node_to_html_node(text_node) for text_node in text_nodes]
                children.append(ParentNode(tag=f'h{level}', children=heading_children))

        elif block_type == BlockType.QUOTE:
            # Strip '>' and parse inline Markdown for each line
            quote_lines = [line[1:].strip() for line in lines if line.strip().startswith('>')]
            if quote_lines:
                text = ' '.join(quote_lines)
                text_nodes = text_to_textnodes(text)
                quote_children = [text_node_to_html_node(text_node) for text_node in text_nodes]
                children.append(ParentNode(tag='blockquote', children=quote_children))

        elif block_type == BlockType.UNORDERED_LIST:
            # Process each list item with inline Markdown
            list_items = []
            for line in lines:
                if line.strip().startswith(('- ', '* ')):
                    item_content = re.sub(r'^[-*]\s+', '', line).strip()
                    if item_content:
                        text_nodes = text_to_textnodes(item_content)
                        item_children = [text_node_to_html_node(text_node) for text_node in text_nodes]
                        list_items.append(ParentNode(tag='li', children=item_children))
            if list_items:
                children.append(ParentNode(tag='ul', children=list_items))

        elif block_type == BlockType.ORDERED_LIST:
            # Process each list item with inline Markdown
            list_items = []
            for line in lines:
                if re.match(r'^\d+\.\s+', line.strip()):
                    item_content = re.sub(r'^\d+\.\s+', '', line).strip()
                    if item_content:
                        text_nodes = text_to_textnodes(item_content)
                        item_children = [text_node_to_html_node(text_node) for text_node in text_nodes]
                        list_items.append(ParentNode(tag='li', children=item_children))
            if list_items:
                children.append(ParentNode(tag='ol', children=list_items))

        elif block_type == BlockType.CODE:
            # Remove ``` delimiters, strip leading/trailing whitespace from each line, ensure trailing newline
            code_lines = [line.lstrip() for line in lines[1:-1]]  # Remove leading whitespace
            code_content = '\n'.join(code_lines) + '\n'  # Add trailing newline
            if code_content.strip():
                code_node = LeafNode(tag='code', value=code_content)
                children.append(ParentNode(tag='pre', children=[code_node]))

    return ParentNode(tag='div', children=children)

    
