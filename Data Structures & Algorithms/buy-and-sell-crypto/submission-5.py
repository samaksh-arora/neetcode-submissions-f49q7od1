class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = min(prices)
        minIndex = prices.index(minValue)
        while minIndex == (len(prices)-1):
            last = prices.pop()
            if len(prices) == 0:
                return 0
            minValue = min(prices)
            minIndex = prices.index(minValue)
        maxDiff = 0; 
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if (prices[j] - prices[i]) > maxDiff:
                    maxDiff = (prices[j] - prices[i])
        return maxDiff
                
        
            

