"""
Question:

Given an integer array nums, return the number of longest increasing subsequences.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
"""
# num_of_LIS_673.py

import pytest
from typing import List

class Solution:
    def find_number_of_LIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        length = [1]*n
        count = [1] * n
        
        lis = 1
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
                        
            lis = max(lis, length[i])
            
        num_lis = 0
        for i in range(n):
            if length[i] == lis:
                num_lis += count[i]
                
        return num_lis


@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, ans", [([1,3,5,4,7], 2), ([2,2,2,2,2], 5)])
def test_find_number_of_LIS(arr, ans):
    sol1 = Solution()
    assert sol1.find_number_of_LIS(arr) == ans

# pytest daily_coding_challenge/october_2020/num_of_LIS_673.py --maxfail=4
