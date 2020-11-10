"""
Question:
Given the root of a binary tree, find the maximum value V for which there exist different nodes 
'A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or 
any child of A is an ancestor of B.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        
        self.res = 0
        min_ = float("inf")
        max_ = float("-inf")
        
        def td_dfs(root, min_, max_):
            
            if not root:
                return
            
            #print(root.val, min_, max_, self.res)
            
            max_ = max(max_, root.val)
            min_ = min(min_, root.val)
            self.res = max(self.res, abs(max_ - min_))
            
            td_dfs(root.left, min_, max_)
            td_dfs(root.right, min_, max_)

        td_dfs(root, min_, max_)
        return self.res        