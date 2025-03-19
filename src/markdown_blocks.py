def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result_blocks = []

    for block in blocks:
        block = block.strip()

        if block != "":
            result_blocks.append(block)

    return result_blocks
