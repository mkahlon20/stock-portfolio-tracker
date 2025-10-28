class StockPurchase:
    def __init__(self, stock_symbol, shares, cost_per_share):
        self.stock_symbol = stock_symbol
        self.shares = shares
        self.cost_per_share = cost_per_share

    def __str__(self):
        return f"{self.cost_per_share} ({self.shares} shares)"

__all__ = ['StockPurchase']