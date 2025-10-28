import unittest
import os
import sys
from io import StringIO

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stock_ledger import StockLedger
from src.stock_purchase import StockPurchase

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.ledger = StockLedger()
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_full_workflow(self):
        # Buy some stocks
        self.ledger.buy("AAPL", 20, 45.0)  # 20 shares at $45
        self.ledger.buy("AAPL", 20, 75.0)  # 20 shares at $75
        self.ledger.buy("MSFT", 20, 95.0)  # 20 shares at $95
        
        # Verify purchases
        aapl_entry = self.ledger.get_entry("AAPL")
        msft_entry = self.ledger.get_entry("MSFT")
        
        self.assertIsNotNone(aapl_entry)
        self.assertIsNotNone(msft_entry)
        self.assertEqual(aapl_entry.purchases.size, 2)  # Two AAPL purchases
        self.assertEqual(msft_entry.purchases.size, 1)  # One MSFT purchase
        
        # Test selling
        self.ledger.sell("AAPL", 30, 65.0)  # Sell across two purchase lots
        
        # Verify remaining shares
        aapl_entry = self.ledger.get_entry("AAPL")
        msft_entry = self.ledger.get_entry("MSFT")
        
        remaining_aapl = aapl_entry.purchases.get_front()
        self.assertEqual(remaining_aapl.shares, 10)  # Should have 10 shares left from second lot
        self.assertEqual(remaining_aapl.cost_per_share, 75.0)  # At original $75 price
        
        remaining_msft = msft_entry.purchases.get_front()
        self.assertEqual(remaining_msft.shares, 20)  # MSFT unchanged

if __name__ == '__main__':
    unittest.main()