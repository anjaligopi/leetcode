#Find_the_Smallest_Divisor_Given_a_Threshold_1283.py
"""
Question:
Given an array of integers nums and an integer threshold, we will choose a positive 
integer divisor and divide all the array by it and sum the result of the division. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or 
equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor 
is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [2,3,5,7,11], threshold = 11
Output: 3

"""

import pytest
import math
from typing import List

class Solution:
    def smallest_divisor(self, nums: List[int], threshold: int) -> int:
        
        """
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        
        d = 1
        while compute_sum(d) > threshold:
            d += 1
        
        return d
        """
        
        l, r = 1, max(nums)
        
        while l<=r:
            m = (l+r)//2
            if sum(math.ceil(num / m) for num in nums) > threshold:
                # sum larger than thresh -> we are looking for a larger divisor
                l = m + 1
            else:
                r = m - 1
                
        return l
    

@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "arr, threshold, ans", [([1,2,5,9], 6, 5), ([2,3,5,7,11], 11, 3)]
)
def test_smallest_divisor(arr, threshold, ans):
    sol1 = Solution()
    assert sol1.smallest_divisor(arr, threshold) == ans

# pytest daily_coding_challenge/october_2020/Find_the_Smallest_Divisor_Given_a_Threshold_1283.py --maxfail=4
