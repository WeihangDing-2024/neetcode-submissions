"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = [None for _ in range(100+1)]

        def dfs(node):
            if not node:
                return None
            val = node.val
            if not nodes[val]:
                new_node = Node(val, None)
                nodes[val] = new_node
                for neighbor in node.neighbors:
                    new_neighbor_node = dfs(neighbor)
                    new_node.neighbors.append(new_neighbor_node)
            return nodes[val]
        
        new_root = dfs(node)
        return new_root