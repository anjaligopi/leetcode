"""
Question:

There are some spherical balloons spread in two-dimensional space. For each balloon, 
provided input is the start and end coordinates of the horizontal diameter. 
Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start 
and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. 
A balloon with xstart and xend bursts by an arrow shot at x 
if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. 
An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], 
return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 
(bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 
(bursting the other two balloons).
"""

from typing import List
import pytest


class Solution:
    def find_min_arrow_shots(self, points: List[List[int]]) -> int:

        points = sorted(points, key=lambda x: x[1])

        end = float("-inf")
        count = 0

        for p in points:
            if p[0] > end:
                count += 1
                end = p[1]

        return count


@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "points, ans", [([[10, 16], [2, 8], [1, 6], [7, 12]], 2), ([[1, 2]], 1)]
)
def test_find_min_arrow_shots(points, ans):
    sol1 = Solution()
    assert sol1.find_min_arrow_shots(points) == ans

# pytest daily_coding_challenge/october_2020/minimum_number_of_arrows_to_burs_balloons_452.py --maxfail=4