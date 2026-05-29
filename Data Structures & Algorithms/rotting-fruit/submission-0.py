class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        from collections import deque

        setOfVisitedCells = set()
        numberOfRows = len(grid)
        numberOfCols = len(grid[0])

        queue = deque()
        for currentRow in range(numberOfRows):
            for currentCol in range(numberOfCols):
                if grid[currentRow][currentCol] == 2:
                    queue.append((currentRow,currentCol, 0))
        maxMinuteElapsed = 0
        while queue:
            currentRow, currentCol, currentMinute = queue.popleft()
           
            if currentRow < 0 or currentRow >= numberOfRows:
                continue
            if currentCol < 0 or currentCol >= numberOfCols:
                continue
            if (currentRow,currentCol) in setOfVisitedCells:
                continue
            if grid[currentRow][currentCol] == 0:
                continue
            
            setOfVisitedCells.add((currentRow,currentCol))
            grid[currentRow][currentCol] = 2
            maxMinuteElapsed = max(currentMinute, maxMinuteElapsed)

            queue.append((currentRow -1, currentCol, currentMinute+1))
            queue.append((currentRow + 1, currentCol, currentMinute+1))
            queue.append((currentRow, currentCol - 1, currentMinute+1))
            queue.append((currentRow, currentCol + 1, currentMinute+1))
        

        for currentRow in range(numberOfRows):
            for currentCol in range(numberOfCols):
                if grid[currentRow][currentCol] == 1:
                    return -1

        return maxMinuteElapsed
