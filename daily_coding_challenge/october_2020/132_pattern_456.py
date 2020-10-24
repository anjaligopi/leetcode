"""
Question:
Given an array of n integers nums, a 132 pattern is a subsequence of three integers 
nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with 
the O(n logn) or the O(n) solution?

 
Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

"""

from typing import List
import pytest

class Solution:
    def find_132_pattern(self, nums: List[int]) -> bool:
        
        stack = []
        ak = float("-inf")
        
        for curr in nums[::-1]:
            
            if curr < ak:
                return True
                
            # ele > top of stack - pop and add ele to stack  
            # find the biggest number that's smaller than the curr number.
            # Because you want to maximize the chance that you find something smaller than the number going left.
            while stack and stack[-1] < curr:
                ak = stack.pop()
            
            stack.append(curr)
            #print(stack)
            
        return False


@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, ans", [ ([1,2,3,4], False) , ([3,1,4,2], True) ])
def test_find_132_pattern(arr, ans):
    sol1 = Solution()
    assert sol1.find_132_pattern(arr) == ans

# pytest daily_coding_challenge/october_2020/132_pattern_456.py --maxfail=4 