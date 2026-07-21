class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i] = at this coin ehat is the fewest number of coins that
        # can be used to make up the target
        #recurrence = dp[i] = 1 + dp[amount - currentCoin]
        #for each amount until we get to the target,
        # we compute how many coins it will take to get there (min)

        if not coins:
            return 0
        
        minCoinsNeededAtAmount = [amount + 1] * (amount + 1)  
        minCoinsNeededAtAmount[0] = 0

        for currAmount in range(1,amount+1):
            for coin in coins:
                if coin <= currAmount:
                    minCoinsNeededAtAmount[currAmount] = min(
                        minCoinsNeededAtAmount[currAmount],1 + minCoinsNeededAtAmount[currAmount - coin])
        
        if minCoinsNeededAtAmount[amount] == amount + 1:
            return -1
        
        return minCoinsNeededAtAmount[amount]
