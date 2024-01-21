class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff > 0:
                max_profit = max(max_profit, diff)
            else: left = right
            right +=1

        return max_profit
