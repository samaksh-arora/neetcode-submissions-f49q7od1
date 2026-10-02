class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefixSumToCountMap = {0 : 1}

        currentSum = 0
        result = 0
        for i in range(len(nums)):
            currentSum += nums[i]

            if currentSum % k in prefixSumToCountMap:
                result += prefixSumToCountMap[currentSum%k]
            
            prefixSumToCountMap[currentSum % k] = prefixSumToCountMap.get(currentSum%k,0) +1

        return result
                