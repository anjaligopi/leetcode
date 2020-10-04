"""
Question:
Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
"""

import pytest
from typing import List

class Solution:
    def remove_covered_intervals(self, intervals: List[List[int]]) -> int:
        
        # in case of a tie in the start points, put the longer one to be the first
        # for descending, put a -x[1]
        # also, interval(ans) is maximized if [-inf, +inf] 
        # start point should be the smallest(asc order), end point largets(desc order)
        
        intervals.sort(key = lambda x : (x[0], -x[1]))
        
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]
        
        # include first ele
        cnt = 1
        
        for i in range(1, len(intervals)):
            curr_s = intervals[i][0]
            curr_e = intervals[i][1]
            
            if curr_e > prev_e:
                # not overlapping/covered, so, add to the cnt bcoz it exists
                prev_s = curr_s
                prev_e = curr_e
                cnt += 1

        return cnt

# Leetcode timeout is mostly 3s
@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, ans", 
                        [ ([[1,4],[3,6],[2,8]] , 2),
                        ([[0,10],[5,12]], 2),
                        ])
def test_remove_covered_intervals(arr, ans):
    sol1 = Solution()
    assert sol1.remove_covered_intervals(arr) == ans


# Run using pytest daily_coding_challenge/october_2020/remove_covered_intervals_1288.py --maxfail=4 
