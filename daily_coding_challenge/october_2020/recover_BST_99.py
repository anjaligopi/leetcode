"""
Question:
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def inorder_dfs(root: TreeNode):
            
            if root is None:
                return
            
            # left, root (+ some processing for mismatched BST), right
            
            inorder_dfs(root.left)
            
            # first swap occurence
            if self.prev and self.first is None and root.val < self.prev.val:
                self.first = self.prev
            
            if self.prev and self.first is not None and root.val < self.prev.val:
                self.second = root
            # second swap occurence

            self.prev = root
            
            inorder_dfs(root.right)
        
        self.prev = None
        self.first = None
        self.second = None
        
        inorder_dfs(root)
        
        #print(self.x.val, self.y.val)
        # swap the mismatched values
        self.first.val, self.second.val = self.second.val, self.first.val