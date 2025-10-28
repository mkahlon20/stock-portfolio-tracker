from linked_deque import LinkedDeque

class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = LinkedDeque()

    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)

    def remove_purchase(self):
        return self.purchases.remove_front()

    def equals(self, other):
        return self.stock_symbol == other.stock_symbol

    def display_entry(self):
        current = self.purchases.front
        result = []
        while current:
            purchase = current.get_data()
            result.append(f"{purchase.cost_per_share} ({purchase.shares} shares)")
            current = current.get_next_node()
        return f"{self.stock_symbol}: " + ", ".join(result)