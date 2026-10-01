class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        result = 0
        left = right = 0

        countMap = {}
        maxCount = 0
        sameNum = False
        while left<=right and right < len(s):
            #step1 - add frequency to countMap
            currChar = s[right]
            if not sameNum:
                countMap[currChar] = countMap.get(currChar, 0) + 1
            #step2 - calculate windowLength
            windowLength = (right-left) + 1
            #step3 - Find most Frequent Char Frequenct
            for letter, count in countMap.items():
                maxCount = max(maxCount, count)
            #step4 - check how many swaps needed for current windowLength
            numSwapsNeeded = windowLength - maxCount

            if numSwapsNeeded <= k:
                result = max(result,windowLength)
                right += 1
                sameNum = False
            else:
                countMap[s[left]] -= 1
                left += 1
                sameNum = True
            
        return result