from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        buying_day = 0
        selling_day = None
        profit = 0

        for i in range(1, n):
            previous_price = prices[i - 1]
            price = prices[i]
            # Price decreased or kept the same
            if price - previous_price <= 0:
                # Check if we have a pending sell
                if selling_day is not None:
                    # Increment the total profit
                    profit += prices[selling_day] - prices[buying_day]
                    # Reset selling day
                    selling_day = None
                # Buy on the cheapest day
                buying_day = i
                continue
            # Price increased
            # Sell when the price is more expensive than the purchase price
            selling_day = i
        # When we finish iterating, check if we have a pending sold
        if selling_day is not None:
            profit += prices[selling_day] - prices[buying_day]

        return profit
