import unittest
import os
from main import get_book_text, get_word_count, get_character_count

class TestHelperFunctions(unittest.TestCase):

    def test_get_word_count(self):
        # Test with a basic string
        file_contents = "This is a simple test."
        self.assertEqual(get_word_count(file_contents), 5)

    def test_get_character_count(self):
        # Test character count for a simple string
        file_contents = "Test"
        result = get_character_count(file_contents)
        # Confirm counts (case insensitive)
        self.assertEqual(result["t"], 2)
        self.assertEqual(result["e"], 1)
        self.assertEqual(result["s"], 1)

    def test_get_book_text(self):
        # Test for a known file path (make a temporary file)
        test_file_path = "tests/temp_test_file.txt"
        with open(test_file_path, "w") as test_file:
            test_file.write("Sample text.")
        self.assertEqual(get_book_text(test_file_path), "Sample text.")
        # Test for an invalid file path
        self.assertIsNone(get_book_text("nonexistent.txt"))
        # Cleanup: Delete the file
        os.remove(test_file_path)
        self.assertFalse(os.path.exists(test_file_path))  # Verify it is gone

if __name__ == "__main__":
    unittest.main()
