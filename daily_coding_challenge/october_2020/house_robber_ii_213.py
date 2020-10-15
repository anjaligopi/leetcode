"""
Question:
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a 
security system connected, and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
because they are adjacent houses.
"""
from typing import List
import py
import pytest

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [0 for i in range(len(nums)-1)] # house numbers 1 to n, not 0 to n, so (len)-1
        
        def house_robber(arr, dp):
            for i in range(1, len(arr)): # dp[0] is already populated based on 1 to n-1 or 2 to n
                rob = arr[i] + dp[i-1][1]
                no_rob = max(dp[i-1][0], dp[i-1][1])
                dp[i] = (rob, no_rob)
            return dp[-1]
        
        # (rob, no_rob)
        # rob first house -> 1 to n-1
        dp[0] = (nums[0], 0)
        ans0 = house_robber(nums[0:-1], dp)
        
        # rob 2nd house -> 2 to n
        dp[0] = (nums[1], 0)
        ans1 = house_robber(nums[1:], dp)
        
        # print(ans0, ans1) #(3, 2) (2, 3)
        return max(max(ans0), max(ans1))

@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, ans", [ ([2,3,2], 3), ([1,2,3,1], 4), ([1], 1)])
def test_rob(arr, ans):
    sol1 = Solution()
    assert sol1.rob(arr) == ans

#pytest daily_coding_challenge/october_2020/house_robber_213.py --maxfail=4 