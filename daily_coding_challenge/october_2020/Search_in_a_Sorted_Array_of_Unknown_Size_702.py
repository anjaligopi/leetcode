"""
Question:
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

 

Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = 1
        
        # key is to find the upper bound
        # upper bound r is somewhere where arr[r] > target
        while reader.get(r) < target:
            r *= 2
            
        #print(r)
        while l<=r:
            
            m = (l+r)//2
            
            if reader.get(m) == target:
                return m
            
            elif reader.get(m) > target:
                r = m - 1
                
            else:
                l = m + 1
                
        return -1