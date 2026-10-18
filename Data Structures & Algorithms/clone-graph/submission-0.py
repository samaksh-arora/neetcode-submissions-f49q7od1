"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Node.val
	#Node.neighbors
        oldToNew = {}
        
        if not node:
            return None
        def copy(node):
            if node in oldToNew:
                return oldToNew[node]
            copyNode = Node()
            oldToNew[node] = copyNode
            copyNode.val = node.val
            for neighborNode in node.neighbors:
                copyNode.neighbors.append(copy(neighborNode))
            return copyNode

        return copy(node)



        