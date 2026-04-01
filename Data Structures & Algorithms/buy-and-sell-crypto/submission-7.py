class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxProfit = 0
        for r in range(1,len(prices)):
            while prices[r] < prices[left]:
                left += 1
            currProfit = prices[r] - prices[left]
            maxProfit = max(currProfit, maxProfit)
        return maxProfit

        
            

