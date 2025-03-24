import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Invalid markdown: no title found, title must start with '# '")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as from_file, open(template_path, "r") as template_file:
        markdown_content = from_file.read()
        
        template = template_file.read()
        
        node = markdown_to_html_node(markdown_content)
        html = node.to_html()
        
        title = extract_title(markdown_content)
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)
        template = template.replace('href="/"', f'href="{basepath}"')
        template = template.replace('src="/"', f'src="{basepath}"')

        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        
        with open(dest_path, "w") as dest_file:
            dest_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
