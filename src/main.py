from textnode import TextNode, TextType


def main():
    text_node = TextNode("test", TextType.NORMAL_TEXT, "/test/url")
    print(text_node)

main()