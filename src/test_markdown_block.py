import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_types(self):
            block = "# heading"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
            block = "###### heading 6"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)
            block = "####### not heading"
            self.assertNotEqual(block_to_block_type(block), BlockType.HEADING)
            
            block = "```\ncode\n```"
            self.assertEqual(block_to_block_type(block), BlockType.CODE)
            block = "`-``\ncode\n```"
            self.assertNotEqual(block_to_block_type(block), BlockType.CODE)
            
            block = "> quote\n> more quote"
            self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
            block = "> quote\n<> not quote"
            self.assertNotEqual(block_to_block_type(block), BlockType.QUOTE)
            
            block = "- list\n- items"
            self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
            block = "- not list\n-- items"
            self.assertNotEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
            
            block = "1. list\n2. items"
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
            block = "1. not list\n3. items\n2. items"
            self.assertNotEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
            
            block = "paragraph"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
            block = "# not paragraph"
            self.assertNotEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
