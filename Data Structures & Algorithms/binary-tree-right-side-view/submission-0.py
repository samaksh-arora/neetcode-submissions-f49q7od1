# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Approach - level order traversal, at every level the last value gets added to the array
        # how do you check the last oen in the level
        # if queue is empty after u pop, then its the last one. 

        if not root:
            return []
        queue = deque([(root,0)])
        result = []
        while queue:
            currentNode, level = queue.popleft()
            
            if len(queue) != 0 and currentNode:
                nextItemInQueue, nextItemLevel = queue[0]
                if nextItemLevel > level:
                    result.append(currentNode.val)
            else:	
                result.append(currentNode.val)

            if currentNode.left:
                queue.append((currentNode.left, level+1))
            if currentNode.right:
                queue.append((currentNode.right, level + 1))
            
        return result
