'''
Testing Peronal Library Source Code
'''
# Python Librarys imported for testing

import unittest
from unittest.mock import patch
from io import StringIO

# Import our user made functions for testing
from personal_library import (
    add_book,
    remove_book,
    list_books,
    search_books
)


# Test Class
class testPersonalLibrary(unittest.TestCase):
    # Test case for add_book function
    def test_add_book_normal_case(self):
        library = []
         # pass a value to the system input
        with patch("builtins.input", return_value="Dune"):
            add_book(library)
        self.assertEqual(library, ["Dune"])


# call the test class main method

if __name__ == "__main__":
    unittest.main() 