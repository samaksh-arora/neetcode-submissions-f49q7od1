class Solution:
    def reorganizeString(self, inputString: str) -> str:

        if not inputString:
            return ""
        
        frequencyMap = Counter(inputString)
        maxHeap = []
        for letter, frequency in frequencyMap.items():
            heapq.heappush(maxHeap, (-frequency, letter)) #negate to simulate max heap
        result = []
        previousLetter = (0,'Dummy') 
        while maxHeap:
            freq, letter = heapq.heappop(maxHeap)	
            freq += 1
            result.append(letter)
            if -previousLetter[0] > 0:
                heapq.heappush(maxHeap, previousLetter)
            
            previousLetter= (freq,letter)
        
            if not maxHeap and -previousLetter[0] >0:
                return '' ''
                
        return "".join(result)
