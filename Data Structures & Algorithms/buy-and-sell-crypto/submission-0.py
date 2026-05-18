class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= curr_lowest_price:
                curr_lowest_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - curr_lowest_price)
        return max_profit