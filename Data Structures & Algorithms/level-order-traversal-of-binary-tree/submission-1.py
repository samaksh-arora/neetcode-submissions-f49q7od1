# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        queue = deque([root])
        result = []
        while queue:
            queueLength = len(queue)
            currentLevel = []
            for i in range(queueLength):
                currNode = queue.popleft()
                if currNode:
                    currentLevel.append(currNode.val)
                    if currNode.left:
                        queue.append(currNode.left)
                    if currNode.right:
                        queue.append(currNode.right)
            if currentLevel:
                result.append(currentLevel)
        
        return result
