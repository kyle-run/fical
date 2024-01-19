class StockAccount:
    def __init__(self):
        self.total_cost = 0
        self.total_shares = 0
        self.total_profit = 0

    def buy(self, price, quantity):
        cost = price * quantity
        self.total_cost += cost
        self.total_shares += quantity
        self.total_profit -= cost  # Decrease profit by the cost of buy
        return self.summary()

    def sell(self, price, quantity):
        if quantity > self.total_shares:
            return 'Error: Selling more shares than you own is not allowed.', False
        revenue = price * quantity
        self.total_profit += revenue  # Add revenue to profit for each sell
        profit_from_this_sell = revenue - (self.total_cost / self.total_shares) * quantity
        self.total_shares -= quantity
        self.total_cost -= (self.total_cost / (self.total_shares + quantity)) * quantity
        return self.summary()

    def summary(self):
        profit_rate = (self.total_profit / self.total_cost) * 100 if self.total_cost else float('inf')
        # Check if profit rate is infinity, which occurs when total cost is zero.
        profit_rate_display = '∞' if profit_rate == float('inf') else f'{profit_rate:.2f}'

        return (f"Profit Rate: {profit_rate_display}%, "
                f"Profit: {self.total_profit:.2f}, "
                f"Shares Owned: {self.total_shares}, "
                f"Total Cost: {self.total_cost:.2f}"), self.total_profit


def print_colored(text, profit):
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    color = GREEN if profit > 0 else RED
    print(color + text + RESET)


def main():
    account = StockAccount()

    while True:
        input_str = input(
            "Enter 'b,price,quantity' to buy, 's,price,quantity' to sell, or 'q' to quit: ").lower().strip()
        if input_str == 'q':
            break
        try:
            action, price_str, quantity_str = input_str.split(',')
            price = float(price_str)
            quantity = int(quantity_str)

            if action == 'b':
                result, profit = account.buy(price, quantity)
                print_colored(result, profit)
            elif action == 's':
                result, profit = account.sell(price, quantity)
                print_colored(result, profit)
            else:
                print("Error: Invalid action. Please start with 'b' or 's'.")
        except (ValueError, IndexError):
            print("Error: Invalid input format. Please use 'b,price,quantity' or 's,price,quantity'.")

        print("-" * 50)  # Print dividing line


if __name__ == "__main__":
    main()