# Leetcode 121
# Best Time to Buy and Sell Stock
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[9]
        minIndex = None
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
                minIndex = i

        max = min
        for i in range(minIndex, len(prices)):
            if prices[i] > max:
                max = prices[i]

        if max > min:
            return max - min
        else:
            return 0





if __name__ == "__main__":
    sol = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))

    prices = [7, 8, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
