# Leetcode 121
# Best Time to Buy and Sell Stock
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            curr_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, curr_profit)
            else:
                left = right
            right += 1

        return max_profit






if __name__ == "__main__":
    sol = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))

    prices = [7, 8, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
