class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        leftPtr = 0
        rightPtr = len(heights) - 1
        resultArea =0
        while leftPtr < rightPtr:
            minHeight = min(heights[leftPtr], heights[rightPtr])
            distance = rightPtr - leftPtr
            
            currentArea = minHeight * distance
            print(f"{minHeight} * {distance} = {currentArea}" )
            if heights[leftPtr] < heights[rightPtr]:
                leftPtr += 1
            elif heights[rightPtr] < heights[leftPtr]:
                rightPtr -= 1
            else: 
                leftPtr += 1
                rightPtr -=1 
            
            resultArea = max(currentArea, resultArea)
            print(resultArea)
        return resultArea
            