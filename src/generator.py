import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Invalid markdown: no title found, title must start with '# '")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as from_file, open(template_path, "r") as template_file:
        markdown_content = from_file.read()
        
        template = template_file.read()
        
        node = markdown_to_html_node(markdown_content)
        html = node.to_html()
        
        title = extract_title(markdown_content)
        template = template.replace("{{ Title }}", title)
        template = template.replace("{{ Content }}", html)

        dest_dir_path = os.path.dirname(dest_path)
        if dest_dir_path != "":
            os.makedirs(dest_dir_path, exist_ok=True)
        
        with open(dest_path, "w") as dest_file:
            dest_file.write(template)
