from textnode import TextNode, TextType

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

# Example usage
if __name__ == "__main__":
    old_nodes = [
        TextNode("Hello, world!", TextType.TEXT),
        TextNode("This is a test.", TextType.TEXT)
    ]
    delimiter = ", "
    text_type = TextType.TEXT
    new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
    
    for node in new_nodes:
        print(node.text)       