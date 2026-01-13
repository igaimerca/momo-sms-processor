import unittest
from etl.clean_normalize import normalize_phone, normalize_amount, normalize_date

class TestCleanNormalize(unittest.TestCase):
    def test_normalize_phone(self):
        self.assertEqual(normalize_phone("+250788123456"), "+250788123456")
        self.assertIsNone(normalize_phone("123"))
    
    def test_normalize_amount(self):
        self.assertEqual(normalize_amount("You received 1000.50"), 1000.50)
        self.assertIsNone(normalize_amount("No amount here"))

if __name__ == '__main__':
    unittest.main()

