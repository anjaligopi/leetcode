"""
Question:
A tree is an undirected graph in which any two vertices are connected by exactly one path. 
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges 
where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes 
ai and bi in the tree, you can choose any node of the tree as the root. When you select a 
node x as the root, the result tree has height h. Among all possible rooted trees, 
those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward 
path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when 
the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
"""

from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if len(edges) == 0:
            return [i for i in range(n)]
        
        # {posible_root : [root's children]}
        dic = defaultdict(list)
        
        # top sort
        graph = defaultdict(list)
        in_deg = {node : 0 for node in range(n)}
        
        for to, frm in edges:
            graph[to].append(frm)
            graph[frm].append(to)
            in_deg[to] += 1
            in_deg[frm] += 1
            
        q = [(node, 1) for node in in_deg if in_deg[node] == 1]
        
        while q:
            node, lvl = q.pop(0)
            dic[lvl].append(node)
            
            for nei in graph[node]:
                in_deg[nei] -= 1
                in_deg[node] -= 1
                
                if in_deg[nei] == 1:
                    q.append((nei, lvl+1))
                    
        # last level will be the ans - either one or two root nodes max (centroids)
        # prune the leaves layer by layer
        
        # print(dic) # {1: [0, 1, 2, 5], 2: [3, 4]}   ;   { 1 : [0,2,3], 2 : [1] }
        # print(graph) # {3: [0, 1, 2, 4], 0: [3], 1: [3], 2: [3], 4: [3, 5], 5: [4]}
        
        last_lvl = max(dic)
        return dic[last_lvl]
        