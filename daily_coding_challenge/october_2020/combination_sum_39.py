"""
Question:

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
import pytest
from typing import List

class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:

        """
        # Brute Force (tree unnecessarily long - since all combinations are added)
        ans = set()
        if not candidates:
            return ans
        
        def td_dfs(path, target):
            
            if target == 0:
                # cannot add list to a set
                ans.add(tuple(sorted(path)))
                
            if target < 0:
                return 
            
            for cand in candidates:
                child_path = path + [cand]
                td_dfs(child_path, target - cand)
        
        td_dfs([], target)
        return ans
        """

        # prune using sorted order - tree isn't unneccessarily growing
        ans = []
        if not candidates:
            return ans
        
        def td_dfs(path, target):
            
            if target == 0:
                ans.append(path)
                
            if target < 0:
                return 
            
            for cand in candidates:
                # add in sorted order - pruning - tree is not going to unnecesaarily grow now
                if path and cand >= path[-1]:
                    child_path = path + [cand]
                    td_dfs(child_path, target - cand)
                
                if not path:
                    child_path = path + [cand]
                    td_dfs(child_path, target - cand)
        
        
        td_dfs([], target)
        return ans

# Leetcode timeout is mostly 3s
@pytest.mark.timeout(3)
@pytest.mark.parametrize("arr, target, ans", [ ([2,3,6,7] ,7, [[2,2,3],[7]]), ([1], 1, [[1]]) ])
def test_combination_sum(arr, target, ans):
    sol1 = Solution()
    assert sol1.combination_sum(arr, target) == ans

# Run using pytest daily_coding_challenge/october_2020/combination_sum_39.py --maxfail=4