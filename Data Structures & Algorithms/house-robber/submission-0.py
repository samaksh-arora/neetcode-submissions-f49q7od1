class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxCashPossibleAtEachHouse = [0] * len(nums)
        maxCashPossibleAtEachHouse[0] = nums[0]
        maxCashPossibleAtEachHouse[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxCashPossibleAtEachHouse[i] = max(maxCashPossibleAtEachHouse[i-1], maxCashPossibleAtEachHouse[i-2] + nums[i])

        lastHouseIndex = len(nums) - 1
        return maxCashPossibleAtEachHouse[lastHouseIndex]
