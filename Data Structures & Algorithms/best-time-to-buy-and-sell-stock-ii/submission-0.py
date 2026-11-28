class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            today = prices[i]
            tomorrow = prices[i + 1]
            profit += tomorrow - today if tomorrow > today else 0

        return profit