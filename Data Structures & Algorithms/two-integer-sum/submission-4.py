class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in newDict:
                return [newDict[diff], i]
            newDict[n] = i
