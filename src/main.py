import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from stock_ledger import StockLedger

def main():
    # Create a new stock ledger
    ledger = StockLedger()
    
    print("Welcome to Stock Portfolio Tracker!")
    print("----------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Buy stock")
        print("2. Sell stock")
        print("3. View portfolio")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            try:
                shares = int(input("Enter number of shares: "))
                price = float(input("Enter price per share: $"))
                ledger.buy(symbol, shares, price)
                print(f"\nBought {shares} shares of {symbol} at ${price:.2f}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        
        elif choice == "2":
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            try:
                shares = int(input("Enter number of shares to sell: "))
                price = float(input("Enter selling price per share: $"))
                ledger.sell(symbol, shares, price)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("\nCurrent Portfolio:")
            print("-----------------")
            ledger.display_ledger()
        
        elif choice == "4":
            print("\nThank you for using Stock Portfolio Tracker!")
            break
        
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()