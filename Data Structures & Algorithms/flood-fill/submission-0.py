class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return None
        
        from collections import deque
        
        #[[1,1,1],
      #   [1,1,0],
    #     [1,0,1]]
        def bfs(currentRow,currentCol):
            queue = deque([(currentRow,currentCol)])
            while queue:
                currentRow, currentCol = queue.popleft()
                if currentRow < 0 or currentRow >= numberOfRows:
                    continue
                if currentCol < 0 or currentCol >= numberOfCol:
                    continue
                if (currentRow,currentCol) in setOfVisitedCells:
                    continue
                if image[currentRow][currentCol] != startingColor:
                    continue
                
                setOfVisitedCells.add((currentRow,currentCol))
                image[currentRow][currentCol] = color

                queue.append((currentRow - 1, currentCol))
                queue.append((currentRow + 1, currentCol))
                queue.append((currentRow, currentCol - 1))
                queue.append((currentRow, currentCol + 1))

        startingColor = image[sr][sc]
        setOfVisitedCells = set()
        numberOfRows = len(image)
        numberOfCol = len(image[0])

        bfs(sr,sc)

        return image
        
                