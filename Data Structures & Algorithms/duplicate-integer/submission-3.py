class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for number in nums:
            if number in numberSet:
                return True
            else:
                numberSet.add(number)
        return False
