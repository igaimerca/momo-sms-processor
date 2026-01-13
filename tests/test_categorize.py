import unittest
from etl.categorize import categorize_transaction

class TestCategorize(unittest.TestCase):
    def test_categorize_deposit(self):
        tx = {"body": "You received 1000 RWF"}
        self.assertEqual(categorize_transaction(tx), "deposit")
    
    def test_categorize_withdrawal(self):
        tx = {"body": "You sent 500 RWF"}
        self.assertEqual(categorize_transaction(tx), "withdrawal")

if __name__ == '__main__':
    unittest.main()

