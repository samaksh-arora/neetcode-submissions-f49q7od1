class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prevMax = nums[0]
        prevMin = nums[0]
        absoluteMax = nums[0]

        for i in range(1,len(nums)):
            currentNumber = nums[i]

            currMax = max(currentNumber, prevMax * currentNumber, prevMin * currentNumber)
            currMin = min(currentNumber, prevMax * currentNumber, prevMin * currentNumber)

            prevMax = currMax
            prevMin = currMin

            absoluteMax = max(absoluteMax, currMax)
        
        return absoluteMax
        