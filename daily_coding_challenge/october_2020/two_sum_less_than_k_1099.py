"""
Question:
Given an array A of integers and integer K, return the maximum S such that 
there exists i < j with A[i] + A[j] = S and S < K. If no i, j 
exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.
 

Constraints:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""

from typing import List

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        A.sort()
        ans = float("-inf")
        
        lo = 0
        hi = len(A)-1
        
        while lo<hi:
            sum_= A[lo] + A[hi]
            if sum_< K:
                ans = max(ans, sum_)
                lo += 1
            else:
                hi -= 1
                
        return ans if ans!= float("-inf") else -1
            