# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        #print(root)
        if not root:
            return None
        
        #encode root node
        root_node = TreeNode(root.val)
        
        #Identif first child and make it left child of root
        #call encode on this child
        if len(root.children) > 0:
            first_child = root.children[0]
            root_node.left = self.encode(first_child)
        
        #Make left child of root (first node in children) the parent for the rest of the children
        curr = root_node.left
        
        # encode the rest of the children as right
        #Change curr to first right node to continue with the rest of the tree
        for i in range(1,len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right
        #print(root_node)
        return root_node
        
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        
        root_node = Node(data.val, [])
        
        curr = data.left
        while curr:
            root_node.children.append(self.decode(curr))
            curr = curr.right
            
        return root_node
        