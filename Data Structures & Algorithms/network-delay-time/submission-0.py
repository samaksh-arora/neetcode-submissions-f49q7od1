class Solution:
    def networkDelayTime(self, times: List[List[int]], numberOfNodes: int, startNode: int) -> int:
        #step1 : make a directed Grap
	
        nodeToOtherNodesMap = {}
        
        for node in range(1,numberOfNodes+1):
            nodeToOtherNodesMap[node] = []
        
        for sourceNode, targetNode, timeTaken in times:
            nodeToOtherNodesMap[sourceNode].append((targetNode, timeTaken))

        #Step2: Graph adjacency list is now built. Now run Dijkstra on the built graph.

        finalMap = {}
        minHeap = []
        heapq.heappush(minHeap, (0,startNode))

        while minHeap:
            currentTime,  currentNode = heapq.heappop(minHeap)

            if currentNode in finalMap:
                continue

            finalMap[currentNode] = currentTime
                
            for neighborNode, timeTaken in nodeToOtherNodesMap[currentNode]:
                if neighborNode not in finalMap:
                    heapq.heappush(minHeap, (timeTaken + currentTime, 
            neighborNode))


        totalTime = 0
        for node in range(1,numberOfNodes+1):
            if node not in finalMap:
                return -1
            totalTime = max(totalTime,finalMap[node])

        return totalTime
	
