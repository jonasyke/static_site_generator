import os
import shutil
import logging
from utils import extract_title, generate_page


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
        logging.info(f"Deleted existing directory: {dst}")

    os.mkdir(dst)
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
    public_dir = "public"

    if not os.path.exists(static_dir):
        logging.error(f"Source directory {static_dir} does not exist.")
        return
    
    copy_directory(static_dir, public_dir)
    logging.info("Directory copy completed successfully.")

    # Generate a page from content/index.md using templates.html and write it to public/index.html
    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path=os.path.join(public_dir, "index.html")
    )





if __name__ == "__main__":
    main()
