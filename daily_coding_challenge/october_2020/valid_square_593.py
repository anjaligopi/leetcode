"""
Question:
Given the coordinates of four points in 2D space, return whether the 
four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array 
with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

"""

from typing import List
import pytest

class Solution:
    def valid_square(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        if p1 == p2 == p3 == p4:
            return False
        
        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2
        
        
        # for square, sides and diagonal must be equal. Only sides is just rhombus
        # If you sort, you get 4 sides first and then diags
        
        lis = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        lis.sort()
        
        print(lis)
        
        if lis[0] == lis[1] == lis[2] == lis[3]: # sides
            if lis[4] == lis[5]: # diagonal
                return True
            
        return False
        

@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "p1, p2, p3, p4, ans", [([0,0], [1,1,], [1,0], [0,1], True)]
)
def test_valid_square(p1, p2, p3, p4, ans):
    sol1 = Solution()
    assert sol1.valid_square(p1, p2, p3, p4) == ans

# pytest daily_coding_challenge/october_2020/valid_square_593.py --maxfail=4