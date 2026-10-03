class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #basically what we will do is have a new array that holds the 
        #prefix product of each index and multiply that with the suffix product

        if not nums:
            return []
        
        resultArray = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            resultArray[i] = prefix
            prefix *= nums[i]
            
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            resultArray[i] *= suffix
            suffix *= nums[i]
    
        
        return resultArray