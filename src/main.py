import os
import sys
import shutil
import logging
from utils import generate_pages_recursive

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
        logging.info(f"Deleted existing directory: {dst}")
    os.makedirs(dst)
    logging.info(f"Created directory: {dst}")

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
            logging.info(f"Copied file: {src_path} to {dst_path}")
        elif os.path.isdir(src_path):
            copy_directory(src_path, dst_path)

def main():
    static_dir = "static"
    doc_dir = "docs"
    # Set basepath for GitHub Pages; use '/' for local testing, '/static_site_generator/' for deployment
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/static_site_generator/"

    if not os.path.exists(static_dir):
        logging.error(f"Source directory {static_dir} does not exist.")
        return
    
    copy_directory(static_dir, doc_dir)
    logging.info("Directory copy completed successfully.")

    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path=doc_dir,
        root_content_path=None,
        basepath=basepath.rstrip('/')  # Ensure no trailing slash for consistency
    )

if __name__ == "__main__":
    main()