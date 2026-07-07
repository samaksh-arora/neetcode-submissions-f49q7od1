class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = []
        for i in range(len(nums)):
            current_num = nums[i]
            if nums[i] > 0:
                break
        
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            leftPtr = i + 1
            rightPtr = len(nums) - 1
            while leftPtr < rightPtr:
                currentSum = nums[i] + nums[leftPtr] + nums[rightPtr]

                if currentSum > 0:
                    rightPtr -= 1
                elif currentSum < 0:
                    leftPtr += 1
                
                else:
                    result.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    rightPtr -= 1
                    while nums[leftPtr] == nums[leftPtr-1] and leftPtr < rightPtr:
                        leftPtr +=1
                
        return result
            
