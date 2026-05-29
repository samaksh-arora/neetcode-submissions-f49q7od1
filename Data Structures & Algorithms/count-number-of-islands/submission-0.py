class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markEntireIsland(currentRow, currentCol):
            if currentRow<0 or currentRow >= numberOfRows:
                return
            if currentCol<0 or currentCol >= numberOfCols:
                return
            if (currentRow,currentCol) in setOfVisitedCells:
                return
            if grid[currentRow][currentCol] == "0":
                return
            
            setOfVisitedCells.add((currentRow,currentCol))

            markEntireIsland(currentRow-1, currentCol)
            markEntireIsland(currentRow+1, currentCol)
            markEntireIsland(currentRow, currentCol+1)
            markEntireIsland(currentRow, currentCol-1)

        if not grid:
            return 0
        
        setOfVisitedCells = set()

        numberOfIslands = 0

        numberOfRows = len(grid)
        numberOfCols = len(grid[0])

        for currentRow in range(numberOfRows):
            for currentCol in range(numberOfCols):
                if grid[currentRow][currentCol] == "1" and (currentRow,currentCol) not in setOfVisitedCells:
                    numberOfIslands+=1
                    markEntireIsland(currentRow,currentCol)
        
        return numberOfIslands
