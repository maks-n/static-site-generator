import os
import shutil
import sys

from copy_files import copy_files_recursive
from generator import generate_pages_recursive

dir_path_public = "./docs"
dir_path_static = "./static"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(f"Deleting {dir_path_public} directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print(f"Copying files from {dir_path_static} to {dir_path_public} directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()
