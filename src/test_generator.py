import unittest

from generator import extract_title

class TestGenerator(unittest.TestCase):
    def test_extract_title_correct(self):
        markdown = "# title"
        self.assertEqual(extract_title(markdown), "title")
    def test_extract_title_double_hash(self):
        markdown = "## double title"
        with self.assertRaises(ValueError):
            extract_title(markdown)
    def test_extract_title_whitespace_before_hash(self):
        markdown = " # whitespace title"
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
