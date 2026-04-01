class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res =[]
        prod = 1
        zeroCount = 0
        for i in range(len(nums)):
                if nums[i] != 0:
                    prod *= nums[i]
                else:
                    zeroCount += 1
        for i in range(len(nums)):
            if zeroCount>1:
                res.append(0)
            elif zeroCount == 1:
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod//nums[i])
            
        return res