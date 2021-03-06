"""
Question:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is 
no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space 
does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function 
should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected 
by the next pointers, with '#' signifying the end of each level.
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        # if root.left exists, root.right is guaranteed to exist as it's a perfect bin tree
        if root.left:
            root.left.next = root.right
            
        # Imagine the 2nd and 3rd levels to find the next of the right node
        if root.right and root.next: # 2nd level
            root.right.next = root.next.left # 3rd level
        
        self.connect(root.left)
        self.connect(root.right)
        return root