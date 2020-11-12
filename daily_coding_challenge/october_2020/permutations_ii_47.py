"""
Question:

Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        
        if not nums:
            return ans
        
        def get_nei(node):
            
            nei_list = []
            
            # node is a list of indices (unique) and not the ele - to avoid duplicates
            for i in range(len(nums)):
                if i not in node:
                    nei_list.append(node + [i])
            
            return nei_list
        
        def td_dfs(node):
            
            # node is a list of indices (unique) and not the ele - to avoid duplicates
            if len(node) == len(nums):
                # always add immuteable ele to a set
                ans.add(tuple(nums[i] for i in node))
            
            for nei in get_nei(node):
                td_dfs(nei)
        
        td_dfs([])
        
        return ans