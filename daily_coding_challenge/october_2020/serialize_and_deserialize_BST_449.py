"""
Question:
Serialization is converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or 
transmitted across a network connection link to be reconstructed later 
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/
deserialization algorithm should work. You need to ensure that a
binary search tree can be serialized to a string,
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.


Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # pre-order traversal
        if not root:
            return ""
        
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        return str(root.val) + " " + left_str + " " + right_str
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        #print(data)
        q = [int(x) for x in data.split(" ") if x]
        #print(q)
        
        def dfs(q, min_, max_):
            
            if not q:
                return None
            
            if q[0] > min_ and q[0] < max_:
                # preorder -> q[0] is the root/first node is the root
                # all values < root in this q will be on the left
                node = TreeNode(q.pop(0))
                node.left = dfs(q, min_, node.val)
                node.right = dfs(q, node.val, max_)
                return node
                
        
        return dfs(q, float("-inf"), float("inf"))
    
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans