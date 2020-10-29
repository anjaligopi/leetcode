"""
Question:
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

import pytest
from typing import List

class Solution:
    def summary_ranges(self, nums: List[int]) -> List[str]:
        
        ans = []
        
        def write_res(s, e):
            result = "%s->%s" %(nums[s], nums[e]) if s != e else "%s"%(nums[s])
            ans.append(result)
            
        if len(nums) == 0:
            return ans

        s, e = 0, 1
        
        while e < len(nums):
            if nums[e] != nums[e-1] + 1:
                write_res(s, e-1)
                s = e
            e += 1
            
        write_res(s, e-1)
        return ans



@pytest.mark.timeout(3)
@pytest.mark.parametrize("nums, ans", [ ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"])])
def test_summary_ranges(nums, ans):
    sol1 = Solution()
    assert sol1.summary_ranges(nums) == ans

    """
    Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""
# pytest daily_coding_challenge/october_2020/summary_ranges_228.py --maxfail=4