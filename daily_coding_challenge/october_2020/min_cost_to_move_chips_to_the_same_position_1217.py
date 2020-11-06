"""
Question:
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position 
of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

 
Example:

Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at poistion 3 to position 2. 
Each move has cost = 1. The total cost = 2.

Input: position = [1,1000000000]
Output: 1
"""

#min_cost_to_move_chips_to_the_same_position_1217.py
import pytest
from typing import List

class Solution:
    def min_cost_to_move_chips(self, position: List[int]) -> int:
        
        even, odd = 0, 0
        
        for x in position:
            if x%2 == 0:
                even += 1
            else:
                odd += 1
                
        return min(odd, even)


@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "arr, ans", [([1,2,3], 1), ([2,2,2,3,3], 2), ([1,1000000000], 1)]
)
def test_min_cost_to_move_chips(arr, ans):
    sol1 = Solution()
    assert sol1.min_cost_to_move_chips(arr) == ans

# pytest daily_coding_challenge/october_2020/min_cost_to_move_chips_to_the_same_position_1217.py --maxfail=4