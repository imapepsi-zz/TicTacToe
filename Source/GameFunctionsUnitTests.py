import unittest
from GameFunctions import *

class MyTestCase(unittest.TestCase):
    def testGetUserLetter(self):
        letter = getUserLetter()
        self.assertEqual(True, letter.isalpha())

    def testGetCompLetter(self):
        self.assertEqual(None, getCompLetter("H"))
        self.assertEqual("X", getCompLetter("O"))
        self.assertEqual("O", getCompLetter("X"))


if __name__ == '__main__':
    unittest.main()
