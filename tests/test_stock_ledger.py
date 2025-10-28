import unittest
import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stock_ledger import StockLedger
from src.stock_purchase import StockPurchase
from src.ledger_entry import LedgerEntry

class TestStockLedger(unittest.TestCase):
    def setUp(self):
        self.stock_ledger = StockLedger()

    def test_empty_ledger(self):
        self.assertEqual(len(self.stock_ledger.entries), 0)

    def test_add_purchase(self):
        stock_purchase = StockPurchase("AAPL", 10, 100.0)  # 10 shares at $100 each
        self.stock_ledger.buy("AAPL", 10, 100.0)
        self.assertTrue(self.stock_ledger.contains("AAPL"))
        entry = self.stock_ledger.get_entry("AAPL")
        self.assertIsNotNone(entry)
        self.assertEqual(entry.stock_symbol, "AAPL")

    def test_sell_stock_fifo(self):
        # Add multiple purchases
        # Buy some stocks
        self.stock_ledger.buy("AAPL", 10, 100.0)
        self.stock_ledger.buy("AAPL", 5, 150.0)
        self.stock_ledger.buy("GOOG", 2, 500.0)
        
        # Verify purchases
        aapl_entry = self.stock_ledger.get_entry("AAPL")
        msft_entry = self.stock_ledger.get_entry("GOOG")
        
        self.assertIsNotNone(aapl_entry)
        self.assertIsNotNone(msft_entry)
        
        # Sell some AAPL shares
        self.stock_ledger.sell("AAPL", 12, 200.0)  # Should sell all 10 from first purchase and 2 from second
        
        # Check remaining shares (should be 3 shares at $150)
        remaining = aapl_entry.purchases.get_front()
        self.assertEqual(remaining.shares, 3)
        self.assertEqual(remaining.cost_per_share, 150.0)

    def test_sell(self):
        # Add and sell some stock
        self.stock_ledger.buy("AAPL", 10, 100.0)
        self.stock_ledger.sell("AAPL", 5, 150.0)  # Should make $250 profit

        # Verify remaining shares
        entry = self.stock_ledger.get_entry("AAPL")
        self.assertIsNotNone(entry)
        purchase = entry.purchases.get_front()
        self.assertEqual(purchase.shares, 5)

if __name__ == '__main__':
    unittest.main()