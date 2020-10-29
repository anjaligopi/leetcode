"""
Question:
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1
"""

import pytest
from typing import List


class Solution:
    def max_dist_to_closest(self, seats: List[int]) -> int:

        """
        First count # zeros at the front and the back.
        For the middle subsequence, count the max # consecutive zeros.
        """

        l = 0
        r = len(seats) - 1

        # left zeros
        while seats[l] == 0:
            l += 1

        # right zeros
        while seats[r] == 0:
            r -= 1

        # middle zeros -> place 1 at k+1/2 if there are k zeros
        cnt = 0
        max_len = 0

        for i in range(l, r + 1):
            if seats[i] != 0:
                cnt = 0
            else:
                cnt += 1
                max_len = max(max_len, cnt)

        # print(max_len, l, len(seats)-1-r)
        return max((max_len + 1) // 2, l, len(seats) - 1 - r)


@pytest.mark.timeout(3)
@pytest.mark.parametrize("nums, ans", [([1, 0, 0, 0, 1, 0, 1], 2), ([0, 1], 1)])
def test_max_dist_to_closest(nums, ans):
    sol1 = Solution()
    assert sol1.max_dist_to_closest(nums) == ans


# pytest daily_coding_challenge/october_2020/maximum_distance_to_closest_person_849.py --maxfail=4
