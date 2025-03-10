import unittest

from textnode import TextNode, TextType


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
        node = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("World", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_not_eq_with_link(self):
        node = TextNode("Hello", TextType.LINK, "test.com")
        node2 = TextNode("Hello", TextType.LINK, "wrong.net")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
