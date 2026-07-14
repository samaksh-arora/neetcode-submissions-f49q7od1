class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Matrix Graph Problem
        #Intuition:
            # run a dfs from every cell 
                #if its 0 return
                #if its part of visited set - return
                #since grid is surrounded by water we dont need to check for edges
        #Roadblock: how do I know when an island is marked visited
            #So basically after your dfs function is ready, what every cell u encounter is 1 island,
            #since from that cell every connected cell would be marked visited anyway

        #Question How do I know how many cells are being calculaed in the island
            #I would return a count variable from the dfs recursive function. 
            #instead of returning nothing u return in the form of 
        
        def dfs(currentRow, currentCol):
            if currentRow < 0 or currentRow >= numberOfRows:
                return 0
            if currentCol < 0 or currentCol >= numberOfCols:
                return 0
            if grid[currentRow][currentCol] == 0:
                return 0
            if (currentRow,currentCol) in setOfVisitedCells:
                return 0
            
            setOfVisitedCells.add((currentRow,currentCol))

            return (1 + 
            dfs(currentRow -1, currentCol) + 
            dfs(currentRow + 1, currentCol) + 
            dfs(currentRow, currentCol -1) + 
            dfs(currentRow, currentCol +1))

        if not grid:
            return 0
        
        setOfVisitedCells = set()
        numberOfRows = len(grid)
        numberOfCols = len(grid[0])
        maxArea = 0
        for currentRow in range(numberOfRows):
            for currentCol in range(numberOfCols):
                if grid[currentRow][currentCol] == 1 and (currentRow,currentCol) not in setOfVisitedCells:
                    maxArea = max(maxArea,dfs(currentRow, currentCol))

        return maxArea