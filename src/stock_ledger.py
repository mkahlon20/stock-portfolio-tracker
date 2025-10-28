from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase

class StockLedger:
    def __init__(self):
        self.entries = []

    def contains(self, stock_symbol):
        return any(entry.stock_symbol == stock_symbol for entry in self.entries)

    def get_entry(self, stock_symbol):
        for entry in self.entries:
            if entry.stock_symbol == stock_symbol:
                return entry
        return None

    def buy(self, stock_symbol, shares_bought, price_per_share):
        if self.contains(stock_symbol):
            entry = self.get_entry(stock_symbol)
            entry.add_purchase(StockPurchase(stock_symbol, shares_bought, price_per_share))
        else:
            entry = LedgerEntry(stock_symbol)
            entry.add_purchase(StockPurchase(stock_symbol, shares_bought, price_per_share))
            self.entries.append(entry)

    def sell(self, stock_symbol, shares_sold, price_per_share):
        if not self.contains(stock_symbol):
            print(f"No shares of {stock_symbol} to sell")
            return

        entry = self.get_entry(stock_symbol)
        total_shares_sold = shares_sold
        profit = 0

        while shares_sold > 0 and entry.purchases.size > 0:
            purchase = entry.purchases.get_front()
            if purchase.shares <= shares_sold:
                shares_sold -= purchase.shares
                profit += purchase.shares * (price_per_share - purchase.cost_per_share)
                entry.remove_purchase()
            else:
                profit += shares_sold * (price_per_share - purchase.cost_per_share)
                purchase.shares -= shares_sold
                shares_sold = 0

        print(f"Sold {total_shares_sold} shares of {stock_symbol} for profit/loss: {profit}")

    def display_ledger(self):
        print("---- Stock Ledger ----")
        if not self.entries:
            print("Portfolio is empty")
            return
            
        for entry in self.entries:
            total_shares = sum(purchase.shares for purchase in entry.purchases)
            if total_shares > 0:
                print(f"\nStock: {entry.stock_symbol}")
                print(f"Total Shares: {total_shares}")
                print("\nPurchase Details:")
                print("-----------------")
                for purchase in entry.purchases:
                    print(f"  Shares: {purchase.shares}, Cost per share: ${purchase.cost_per_share:.2f}")
            print(entry.display_entry())
        print()
