from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        frqCount = Counter(nums)

        maxCount = 1
        maxNum = nums[0]
        print (frqCount)
        for key, value in frqCount.items():
            if value > maxCount:
                maxCount = max(maxCount, value)
                maxNum = key
        
        return maxNum
            