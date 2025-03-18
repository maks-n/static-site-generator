from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, alt=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt = alt

    def __eq__(self, other):
        if self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url and self.alt == other.alt:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node is None:
        raise Exception("TextNode is None")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise Exception(f"TextNode IMAGE missing URL, text: {text_node.text}")
            if text_node.alt is None:
                raise Exception(f"TextNode IMAGE missing alt, text: {text_node.text}")
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.alt})
        case _:
            raise Exception("Unknown TextType of the TextNode")
