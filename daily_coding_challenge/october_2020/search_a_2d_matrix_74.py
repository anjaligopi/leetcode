"""
Question:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
"""

import pytest
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        def bin_search(row):
            l = 0
            r = len(row)-1
        
        # find row
        row = 0
        for r in range(len(matrix)):
            #print(r)
            if target > matrix[r][0] and target < matrix[r][-1]:
                row = r
                break
            elif target == matrix[r][0] or target == matrix[r][-1]:
                return True
        
        # Bin search in the row for the target
        l = 0
        r = len(matrix[row]) - 1
        
        while l<=r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False