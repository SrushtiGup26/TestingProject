import unittest
from src.model import detect_spam

class TestSpamDetection(unittest.TestCase):

    def test_spam_message(self):
        self.assertEqual(detect_spam("You have won a free prize!"), "This message is likely spam!")

    def test_legitimate_message(self):
        self.assertEqual(detect_spam("Hello, how are you?"), "This message seems to be legitimate.")

if __name__ == '__main__':
    unittest.main()
