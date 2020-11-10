"""
Question:
Given a binary matrix A, we want to flip the image horizontally, then invert it, 
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""

import pytest
from typing import List

class Solution:
    def flip_and_invert_image(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(A)):
            A[i] = A[i][::-1] # reverse each row
            
            for j in range(len(A)): # invert each element
                if A[i][j] == 0:
                    A[i][j] = 1
                    
                else:
                    A[i][j] = 0
                    
        return A



@pytest.mark.timeout(3)
@pytest.mark.parametrize(
    "inp, outp", [([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])]
)
def test_flip_and_invert_image(inp, outp):
    sol1 = Solution()
    assert sol1.flip_and_invert_image(inp) == outp

# pytest daily_coding_challenge/october_2020/flipping_an_img_832.py --maxfail=4