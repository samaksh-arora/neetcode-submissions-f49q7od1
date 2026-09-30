class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumToCountMap = {0 : 1}

        currentSum = 0
        result = 0
        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum - k in prefixSumToCountMap:
                result += prefixSumToCountMap[currentSum-k]
            
            prefixSumToCountMap[currentSum] = prefixSumToCountMap.get(currentSum,0) +1
        return result
                


        
