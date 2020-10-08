"""
Question:
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

import pytest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        if len(nums) == 1 and target not in nums:
            return -1
        
        if len(nums) == 1 and target in nums:
            return 0
        
        l = 0
        r = len(nums)-1
        
        while l<=r:
            
            m = (l+r)//2
            
            if nums[m] == target:
                return m
            
            elif nums[m] < target:
                l += 1
                
            else:
                r -= 1
                
        return -1

@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, target, ans", [([-1,0,3,5,9,12] , 9, 4), ([-1,0,3,5,9,12], 2, -1)])
def test_search(arr, target, ans):
    sol1 = Solution()
    assert ans == sol1.search(arr, target)

# pytest daily_coding_challenge/october_2020/number_of_recent_calls_933.py --maxfail=4