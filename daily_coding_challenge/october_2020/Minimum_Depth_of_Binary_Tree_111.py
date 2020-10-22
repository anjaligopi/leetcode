"""
Question:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        q = [(root, 1)]
        
        while q:
            
            node, step = q.pop(0)
            
            if node.left is None and node.right is None:
                return step
            
            if node.left:
                q.append((node.left, step+1))
            
            if node.right:
                q.append((node.right, step+1))