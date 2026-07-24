class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        adjanceyList = {node: set() for node in range(n)}
        for edge in edges:
            nodeA = edge[0]
            nodeB = edge[1]
            adjanceyList[nodeA].add(nodeB)
            adjanceyList[nodeB].add(nodeA)

        def dfs(currentNode):
            if len(adjanceyList[currentNode]) == 0:
                return 
            
            if currentNode in setOfVisitedCells:
                return
            
            setOfVisitedCells.add(currentNode)

            for node in adjanceyList[currentNode]:
                dfs(node)
            
        setOfVisitedCells = set()

        count = 0
        
        for node in range(n):
            if node not in setOfVisitedCells:
                count += 1
                dfs(node)
        
        return count

                