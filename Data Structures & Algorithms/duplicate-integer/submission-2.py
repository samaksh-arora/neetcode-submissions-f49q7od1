class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = set(nums)
        return not (len(setList) == len(nums))