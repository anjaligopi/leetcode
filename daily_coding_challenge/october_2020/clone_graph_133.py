"""
Question:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
"""

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    
    def __init__(self):
        # {old_node : new_node}
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val)
        self.visited[node] = new_node # add new_node to dict, otherwise, infinte loop
        if node.neighbors:
            for nei in node.neighbors:
                new_node.neighbors.append(self.cloneGraph(nei))
                
        return self.visited[node]