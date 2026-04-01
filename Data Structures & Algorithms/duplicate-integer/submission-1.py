class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet = set(nums)
        if len(nums) != len(newSet):
            return True
        return False  