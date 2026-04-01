class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        numCount = {}
        for num,count in freq.items():
            if count not in numCount:
                numCount[count] = []
            numCount[count].append(num)
    
        result = []
        freqArray = sorted(list(numCount.keys()))
        while len(result) < k:
            if freqArray:
                nextValFreq = freqArray.pop()
                nextVals = numCount[nextValFreq]
                result.extend(nextVals)
            else:
                return result
        return result[:k]