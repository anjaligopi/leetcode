"""
Question:
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. 
You can return any of them.
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
"""

import pytest
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def convert_lst_to_tree(lst: List[int]):
        #from_list is the ideal way to name this function
        # convert list to tree
        if not lst:
            return None

        node_lst = [TreeNode(val) for val in lst]
        
        for i in range(len(node_lst)):
            root = node_lst[i] # n, 2n+1, 2n+2 -> root, left, right indices -> level order
            if 2*i + 1 < len(node_lst):
                if node_lst[2*i + 1].val is not None:
                    root.left = node_lst[2*i + 1]
            if 2*i + 2 < len(node_lst):
                if node_lst[2*i + 2].val is not None:
                    root.right = node_lst[2*i + 2]
        return node_lst[0]

    def to_list(self):
        # tree to list
        lvl_dic = {}

        def td_dfs(node, i):
            if not node:
                return None

            lvl_dic[i] = node.val
            
            td_dfs(node.left, 2*i + 1)
            td_dfs(node.right, 2*i + 2)

        td_dfs(self, 0)

        return [lvl_dic.get(i, None) for i in range(max(lvl_dic)+1)]

class Solution:
    def insert_into_BST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return TreeNode(val)
            
        # insert into the right sub-tree
        if val > root.val:
            root.right = self.insert_into_BST(root.right, val)

        # right  
        else:
            root.left = self.insert_into_BST(root.left, val)
            
        return root

@pytest.mark.parametrize("tree_list, val, ans", [([40,20,60,10,30,50,70], 25, [40,20,60,10,30,50,70,None,None,25]) , 
                                            ([4,2,7,1,3], 5, [4,2,7,1,3,5])])
def test_insert_into_BST(tree_list, val, ans):
    sol1 = Solution()
    root = TreeNode.convert_lst_to_tree(tree_list)
    root = sol1.insert_into_BST(root, val)
    ans_list = root.to_list()
    print("ans root: ", ans_list)
    assert ans_list == ans


# pytest daily_coding_challenge/october_2020/insert_into_bst_701.py --maxfail=4 