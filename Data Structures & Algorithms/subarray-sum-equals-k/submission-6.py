class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumMap = {0:1}
        currentSum = 0
        result = 0
        for number in nums:
            currentSum += number

            diff = currentSum - k
            if diff in prefixSumMap:
                result += prefixSumMap[diff]
            prefixSumMap[currentSum] = prefixSumMap.get(currentSum,0) + 1
            
        return result

        
