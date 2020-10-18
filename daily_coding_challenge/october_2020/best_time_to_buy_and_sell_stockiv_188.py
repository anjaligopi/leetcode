"""
Question:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""

import pytest
from typing import List

class Solution:
    def max_profit(self, prices: List[int], k: int) -> int:
        
        if k < 1:
            return 0
        
        if k > len(prices)//2:
            # k is v big
            s = 0
            for i in range(len(prices)-1):
                profit = prices[i+1] - prices[i]
                if profit > 0:
                    s+= profit
            return s
        
        buy = [float("inf")] * k
        profit = [0] * k
        
        for price in prices:
            gain_profit = 0
            for j in range(len(buy)):
                # reinvest the gained profit
                buy[j]= min(buy[j], price - gain_profit)
                profit[j] = max(profit[j], price - buy[j])
                gain_profit = profit[j]
        
        #print(profit)
        return profit[-1]
                
@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, k, ans", [ ([2,4,1], 2, 2) , ([3,2,6,5,0,3], 2, 7) ])
def test_max_profit(arr, k, ans):
    sol1 = Solution()
    assert sol1.max_profit(arr, k) == ans