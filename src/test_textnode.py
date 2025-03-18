import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_link(self):
        node = TextNode("Hello", TextType.LINK, "test.com")
        node2 = TextNode("Hello", TextType.LINK, "test.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("World", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq_with_link(self):
        node = TextNode("Hello", TextType.LINK, "test.com")
        node2 = TextNode("Hello", TextType.LINK, "wrong.net")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href":"google.com"})
    
    def test_img(self):
        node = TextNode("alt text", TextType.IMAGE, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"google.com", "alt":"alt text"})


if __name__ == "__main__":
    unittest.main()
