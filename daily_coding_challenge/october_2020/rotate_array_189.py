"""
Question:

Given an array, rotate the array to the right by k steps, 
where k is non-negative.

Follow up:

Try to come up as many solutions as you can, 
there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

import pytest
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # nums[:] = nums[len(nums)-k : ] + nums[ 0 : len(nums)-k ]
        return nums
            
@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, k, ans", [ ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]) , ([-1,-100,3,99], 2, [3,99,-1,-100]) ])
def test_rotate(arr, k, ans):
    sol1 = Solution()
    assert sol1.rotate(arr, k) == ans
