"""
Question:
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that 
B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
"""
from typing import List
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        max_len = 0
        
        # don't include 0 and len(A)-1
        # they wont be the peaks (?)
        # two pointers - initialize l,r at the peak first 
        # and then move l to the left and r to the right
        
        for i in range(1, len(A)-1):
            
            if A[i-1] < A[i] > A[i+1]:
                l, r = i, i
                
                while l>0 and A[l-1] < A[l]:
                    l -= 1
                    
                while r+1 < len(A) and A[r] > A[r+1]:
                    r += 1

                max_len = max(max_len, r-l+1)
                
        return max_len