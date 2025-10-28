import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.stock_ledger import StockLedger
from src.stock_purchase import StockPurchase

def main():
    """Quick test script to demonstrate functionality."""
    ledger = StockLedger()
    
    # Add some stock purchases
    ledger.buy("AAPL", 10, 100.0)  # 10 shares at $100 each = $1000 total
    ledger.buy("AAPL", 5, 150.0)   # 5 shares at $150 each = $750 total
    ledger.buy("GOOG", 2, 500.0)   # 2 shares at $500 each = $1000 total
    
    # Print current holdings
    print("\nCurrent Holdings:")
    ledger.display_ledger()
    
    # Sell some AAPL stock and calculate gain
    print("\nSelling 12 AAPL shares at $200 each...")
    ledger.sell("AAPL", 12, 200.0)
    
    # Print final holdings
    print("\nFinal Holdings:")
    ledger.display_ledger()

if __name__ == '__main__':
    main()