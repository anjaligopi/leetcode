"""
Question:
Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
"""

import pytest
from typing import List


class Solution:
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()

        for i in range(len(intervals)):

            if i + 1 < len(intervals) and intervals[i][1] > intervals[i + 1][0]:
                return False

        return True


@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "arr, ans", [([[0, 30], [5, 10], [15, 20]], False), ([[7,10],[2,4]], True)]
)
def test_can_attend_meetings(arr, ans):
    sol1 = Solution()
    assert sol1.can_attend_meetings(arr) == ans


# pytest daily_coding_challenge/october_2020/meeting_rooms_252.py --maxfail=4
