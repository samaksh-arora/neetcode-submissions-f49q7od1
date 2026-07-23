class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Start a dfs from the first character of the word
        #see if the next character is the one we want (from either of the 4 directions)
        
        if not board and not word:
            return True
        if not board:
            return False
        if not word:
            return True
        
        def dfs(currentRow, currentCol, currentIdx):
            if currentIdx == len(word):
                return True
            if currentRow < 0 or currentRow>=numberOfRows:
                return False
            if currentCol < 0 or currentCol >= numberOfCols:
                return False
            if (currentRow,currentCol) in setOfVisitedCells:
                return False
            if board[currentRow][currentCol] != word[currentIdx]:
                return False
            
            setOfVisitedCells.add((currentRow,currentCol))

            pathFound = (dfs(currentRow -1, currentCol, currentIdx + 1) or
            dfs(currentRow +1, currentCol, currentIdx + 1) or
            dfs(currentRow, currentCol - 1, currentIdx + 1) or
            dfs(currentRow , currentCol + 1, currentIdx + 1))

            setOfVisitedCells.remove((currentRow,currentCol))

            return pathFound
        setOfVisitedCells = set()
        numberOfRows = len(board)
        numberOfCols = len(board[0])

        for currentRow in range(numberOfRows):
            for currentCol in range(numberOfCols):
                if board[currentRow][currentCol] == word[0]:
                    if dfs(currentRow,currentCol,0):
                        return True
        
        return False
        



