class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberToIdxMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numberToIdxMap:
                return [ numberToIdxMap[difference], i]
            else:
                numberToIdxMap[nums[i]] = i


