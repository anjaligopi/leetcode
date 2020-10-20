"""
Question:
n a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A 
are the same, or all the values in B are the same.

If it cannot be done, return -1.

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""

import pytest
from typing import List

class Solution:
    def min_domino_rotations(self, A: List[int], B: List[int]) -> int:
        
        if len(A) <= 1:
            return 0
        
        def helper(target, A, B):
            count = 0
            for idx in range(len(A)):
                a, b = A[idx], B[idx]
                if a == target:
                    continue
                else:
                    # target not in a, but could be in b
                    if b == target:
                        count += 1 # swap
                    else:
                        # number not in a or b
                        count = float("inf")
                        break
            return count
        
        res = min(helper(A[0], A, B), helper(A[0], B, A), helper(B[0], A, B), helper(B[0], B, A))
        return res if res != float("inf") else -1
            
@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr1, arr2, ans", [([2,1,2,4,2,2], [5,2,6,2,3,2], 2), ([3,5,1,2,3], [3,6,3,3,4], -1)])
def test_min_domino_rotations(arr1, arr2, ans):
    sol1 = Solution()
    assert sol1.min_domino_rotations(arr1, arr2) == ans

#pytest daily_coding_challenge/october_2020/Minimum_Domino_Rotations_For_Equal_Row_1007.py --maxfail=4 