import unittest
import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ledger_entry import LedgerEntry
from src.stock_purchase import StockPurchase

class TestLedgerEntry(unittest.TestCase):
    def setUp(self):
        self.ledger = LedgerEntry("AAPL")

    def test_initialization(self):
        self.assertEqual(self.ledger.stock_symbol, "AAPL")
        self.assertTrue(self.ledger.purchases.is_empty())

    def test_add_purchase(self):
        purchase = StockPurchase("AAPL", 10, 150.00)
        self.ledger.add_purchase(purchase)
        self.assertFalse(self.ledger.purchases.is_empty())
        front = self.ledger.purchases.get_front()
        self.assertEqual(front.cost_per_share, 150.00)
        self.assertEqual(front.shares, 10)

    def test_remove_purchase(self):
        purchase1 = StockPurchase("AAPL", 10, 150.00)
        purchase2 = StockPurchase("AAPL", 5, 160.00)
        self.ledger.add_purchase(purchase1)
        self.ledger.add_purchase(purchase2)
        
        removed = self.ledger.remove_purchase()
        self.assertEqual(removed.cost_per_share, 150.00)
        self.assertEqual(removed.shares, 10)
        
        remaining = self.ledger.purchases.get_front()
        self.assertEqual(remaining.cost_per_share, 160.00)
        self.assertEqual(remaining.shares, 5)

    def test_equals(self):
        other_ledger = LedgerEntry("AAPL")
        different_ledger = LedgerEntry("GOOGL")
        
        self.assertTrue(self.ledger.equals(other_ledger))
        self.assertFalse(self.ledger.equals(different_ledger))

    def test_display_entry(self):
        purchase1 = StockPurchase("AAPL", 10, 150.00)
        purchase2 = StockPurchase("AAPL", 5, 160.00)
        self.ledger.add_purchase(purchase1)
        self.ledger.add_purchase(purchase2)
        
        expected = "AAPL: 150.0 (10 shares), 160.0 (5 shares)"
        self.assertEqual(self.ledger.display_entry(), expected)

    def test_empty_display(self):
        expected = "AAPL: "
        self.assertEqual(self.ledger.display_entry(), expected)

if __name__ == '__main__':
    unittest.main()