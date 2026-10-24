class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount + 1)

        dp[0] = 0

        for currAmount in range(1,amount+1):
            for coin in coins:
                if coin <= currAmount:
                    dp[currAmount] = min(dp[currAmount],dp[currAmount - coin] + 1)
        
        if dp[amount] == amount + 1:
            return -1
        
        return dp[amount]
    
