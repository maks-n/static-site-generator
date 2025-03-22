def extract_title(markdown):
    if not markdown.startswith("# "):
        raise ValueError("Invalid markdown format: title must start with '# '")
    return markdown[2:].strip()

