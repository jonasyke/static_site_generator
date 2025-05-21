from textnode import TextNode, TextType, extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == text_type:
            parts = node.text.split(delimiter)
            for part in parts:
                new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(node)
            continue

        current_pos = 0
        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            image_start = text.find(image_markdown, current_pos)
            if image_start == -1:
                continue

            if image_start > current_pos:
                new_nodes.append(TextNode(text[current_pos:image_start], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            current_pos = image_start + len(image_markdown)

        if current_pos < len(text):
            new_nodes.append(TextNode(text[current_pos:], TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue

        current_pos = 0
        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            link_start = text.find(link_markdown, current_pos)
            if link_start == -1:
                continue

            if link_start > current_pos:
                new_nodes.append(TextNode(text[current_pos:link_start], TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))

            current_pos = link_start + len(link_markdown)

        if current_pos < len(text):
            new_nodes.append(TextNode(text[current_pos:], TextType.TEXT))

    return new_nodes





