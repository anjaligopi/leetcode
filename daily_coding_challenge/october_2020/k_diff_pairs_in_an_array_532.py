"""
Question:
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k
"""

import collections
import pytest
from typing import List


class Solution:
    def find_pairs(self, nums: List[int], k: int) -> int:

        """
        # Brute Force
        #cnt = 0
        ans = set()
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                #print("loop", nums[i] , nums[j])
                if i != j and nums[j] - nums[i] == k:
                    ans.add((nums[i], nums[j]))
                    #print(nums[j] , nums[i])
        
        #print(ans)
        return len(ans)
        """
        count = collections.Counter(nums)

        if k > 0:
            res = sum([num + k in count for num in count])
        else:
            # k == 0 -> looking for pairs of equal numbers -> so, just check each freq
            res = sum([count[num] > 1 for num in count])
            """
            for num in count:
                #print(res, num, count, count[num])
                #[1,1,1,1], 0 -> (1,1) -> 1
                if count[num] > 1:
                    res += 1
            """
        return res

    """
    [3,1,4,1,5]
    2
 [1,3,1,5,4]
0   
    
    """


# Leetcode timeout is mostly 3s
@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "arr, k, ans",
    [([1, 1, 1, 1], 0, 1), ([3, 1, 4, 1, 5], 2, 2), ([3, 1, -4, 1, -5], 1, 1)],
)
def test_find_pairs(arr, k, ans):
    sol1 = Solution()
    assert sol1.find_pairs(arr, k) == ans


# Run using pytest daily_coding_challenge/october_2020/k_diff_pairs_in_an_array_532.py --maxfail=4 
