class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        count = 0
        for number in nums:
            length = 0
            if number -1 in nums:
                continue
            
            while number + length in nums:
                length +=1 
                count = max(count,length)
            
        return count
