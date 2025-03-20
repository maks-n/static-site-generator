import os
import shutil

from copy_files import copy_files_recursive

dir_path_public = "./public"
dir_path_static = "./static"

def main():
    print("Deleting 'public' directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree("public/")
    
    print("Copying files from 'static' to 'public' directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


main()
