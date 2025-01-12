
class Solution:
    def max_profit(prices):
        max_profit = 0  # Initialize max profit to 0
        n = len(prices)

        # Iterate through all possible buy days
        for buy_day in range(n - 1):
            # Iterate through all possible sell days after the buy day
            for sell_day in range(buy_day + 1, n):
                # Calculate profit
                profit = prices[sell_day] - prices[buy_day]
                # Update max profit if the current profit is greater
                if profit > max_profit:
                    max_profit = profit

        return max_profit