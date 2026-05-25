class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        result = []
        
        integerFrequencyMap = {}
    
        for number in nums:
            integerFrequencyMap[number] = integerFrequencyMap.get(number, 0) + 1
        
        print(integerFrequencyMap)
        listOfFrequencyNumber = []
        for number, frequency in integerFrequencyMap.items() :
            listOfFrequencyNumber.append([frequency,number])
        
        listOfFrequencyNumber.sort()
        print(listOfFrequencyNumber)
        while k > 0:
            result.append(listOfFrequencyNumber.pop()[1])
            k -= 1
        
        return result
        
