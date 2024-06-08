class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        buying_day = 0
        selling_day = None
        solution = []

        for i in range(1, n):
            previous_price = A[i - 1]
            price = A[i]
            # Price decreased or kept the same
            if price - previous_price <= 0:
                # Check if we have a pending sell
                if selling_day is not None:
                    # Append the buying and selling days to the solution
                    solution.append([buying_day, selling_day])
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
            solution.append([buying_day, selling_day])

        return solution
