class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #to see if nums[i] - 1 exists

        result = 0
        for currentNumber in nums:
            length = 1
            if currentNumber - 1 not in numSet:
                while currentNumber + length in numSet:
                    length += 1
                result = max(result, length)
            
        return result