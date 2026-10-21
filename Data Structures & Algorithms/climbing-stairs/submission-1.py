class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i] = number of distinct ways to get to this step
        #dp[0], dp[1] = 1

        #dp[i] = dp[i-1] + dp[i-2]

        if not n:
            return 0
        
        dp = [0] * (n+1)

        dp[0] = dp[1] = 1

        for step in range(2,n+1):
            dp[step] = dp[step-1] + dp[step-2]
        
        print(dp)
        return dp[n]
