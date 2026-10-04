class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        suffix = 0
        suffixArray = []

        for i in range(len(nums)-1,-1,-1):
            suffixArray.append(suffix)
            suffix+=nums[i]
        print(suffixArray)
        suffixArray.reverse()
        prefix = 0
        for i in range(len(nums)):
            if prefix == suffixArray[i]:
                return i
            prefix += nums[i]
        
        
        return -1