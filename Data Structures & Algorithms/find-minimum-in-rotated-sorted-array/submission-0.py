class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        if nums[right] > nums[left]:
            return nums[left]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                return nums[right]
        