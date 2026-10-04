class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        numRows = len(grid)
        numCols = len(grid[0])

        def dfs(currentRow, currentCol):
            if currentRow<0 or currentRow>=numRows:
                return
            if currentCol<0 or currentCol>=numCols:
                return
            if grid[currentRow][currentCol] == "0":
                return
            if (currentRow,currentCol) in setOfVisitedCells:
                return
            
            setOfVisitedCells.add((currentRow,currentCol))

            dfs(currentRow - 1, currentCol)
            dfs(currentRow + 1, currentCol)
            dfs(currentRow, currentCol - 1)
            dfs(currentRow, currentCol + 1)

        setOfVisitedCells = set()
        count = 0
        for row in range(numRows):
            for col in range(numCols):
                if (row,col) not in setOfVisitedCells and grid[row][col] == "1":
                    count+=1
                    dfs(row,col)
        
        return count
