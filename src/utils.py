import re
import os
import logging
from pathlib import Path
from block_markdown import markdown_to_html_node

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_title(markdown):
    """Extract the h1 header from markdown text, stripping # and whitespace."""
    match = re.search(r'^#\s+(.+?)\s*$', markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    raise ValueError("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path, basepath):
    """Generate an HTML page from a Markdown file using a template."""
    logging.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    title = extract_title(markdown_content)
    
    # Replace placeholders
    final_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)
    
    # Fix paths: handle both absolute (/path) and relative (path) URLs
    # Ensure basepath doesn't have leading/trailing slashes for consistency
    basepath = basepath.strip('/')
    if basepath:
        # Replace absolute paths (e.g., href="/about" or href='/about')
        final_content = re.sub(r'href=["\']/([^"\']*)["\']', f'href="/{basepath}/\\1"', final_content)
        final_content = re.sub(r'src=["\']/([^"\']*)["\']', f'src="/{basepath}/\\1"', final_content)
        # Replace relative paths (e.g., href="about" or src="images/pic.jpg")
        final_content = re.sub(r'href=["\']((?!http[s]?://)[^"\']+)["\']', f'href="/{basepath}/\\1"', final_content)
        final_content = re.sub(r'src=["\']((?!http[s]?://)[^"\']+)["\']', f'src="/{basepath}/\\1"', final_content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    logging.info(f"Generated page at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, root_content_path=None, basepath='/'):
    """
    Recursively crawl the content directory and generate HTML files from Markdown using the template.
    Relative paths are always calculated from the top-level root_content_path.
    """
    content_path = Path(dir_path_content)
    dest_path = Path(dest_dir_path)

    if root_content_path is None:
        root_content_path = content_path

    for entry in os.listdir(content_path):
        entry_path = content_path / entry

        if entry_path.is_file() and entry_path.suffix == '.md':
            # Compute relative path from the root
            relative_path = entry_path.relative_to(root_content_path)
            dest_file_path = dest_path / relative_path.with_suffix('.html')
            dest_file_path.parent.mkdir(parents=True, exist_ok=True)
            generate_page(entry_path, template_path, dest_file_path, basepath)

        elif entry_path.is_dir():
            # Recurse with the same root and basepath
            generate_pages_recursive(entry_path, template_path, dest_dir_path, root_content_path, basepath)

