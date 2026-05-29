class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        def bfsMarkEntireIsland(currentRow, currentCol):
            queue = deque([(currentRow,currentCol)])
            while queue:
                currentRow, currentCol = queue.popleft()
                if currentRow < 0 or currentRow >= numberOfRows:
                    continue
                if currentCol < 0 or currentCol >= numberOfCols:
                    continue
                if grid[currentRow][currentCol] == "0":
                    continue 
                if (currentRow, currentCol) in setOfVisitedCells:
                    continue
                
                setOfVisitedCells.add((currentRow,currentCol))

                queue.append((currentRow - 1, currentCol))
                queue.append((currentRow + 1, currentCol))
                queue.append((currentRow, currentCol - 1))
                queue.append((currentRow, currentCol + 1))
        
        if not grid:
            return 0
        
        setOfVisitedCells = set()
        numberOfRows = len(grid)
        numberOfCols = len(grid[0])
        numberOfIslands = 0

        for currentRow in range(numberOfRows):
            for currentCol in range(numberOfCols):
                if (currentRow,currentCol) not in setOfVisitedCells and grid[currentRow][currentCol] == "1":
                    numberOfIslands += 1
                    bfsMarkEntireIsland(currentRow, currentCol)
        

        return numberOfIslands
                
