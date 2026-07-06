class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []

        leftPtr = 0
        rightPtr = len(numbers) - 1
        
        while leftPtr < rightPtr:
            currSum = numbers[leftPtr] + numbers[rightPtr]
            if currSum > target:
                rightPtr -= 1
            if currSum < target:
                leftPtr += 1
            if currSum == target:
                return [leftPtr+1, rightPtr+1]
            
        return [ ]

            