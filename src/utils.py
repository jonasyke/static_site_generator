import re
import os
import logging
from block_markdown import markdown_to_html_node

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_title(markdown):
    """Extract the h1 header from markdown text, stripping # and whitespace."""
    match = re.search(r'^#\s+(.+?)\s*$', markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    raise ValueError("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path):
    """Generate an HTML page from a Markdown file using a template."""
    logging.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    print(f"Generated HTML content: {html_content[:200]}...")  # First 200 chars

    title = extract_title(markdown_content)
    
    final_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    logging.info(f"Generated page at {dest_path}")

generate_page("content/index.md", "template.html", "public/index.html")