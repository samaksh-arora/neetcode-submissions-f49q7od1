class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp[row][col] = dp[row-1][col] + dp[row][col-1]
        #dp[row][col] = number of paths u can take to that cell

        dp = [[0] * n] * m
        print(dp)
        dp[0][0] = 0
        for col in range(1,len(dp[0])):
            dp[0][col] = 1
        for row in range(0, len(dp)):
            dp[row][0] = 1
        
        print(dp)
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[len(dp)-1][len(dp[0])-1]
