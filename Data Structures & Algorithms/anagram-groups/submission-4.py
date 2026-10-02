class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Approach
        #all anagrams will have same amount of letters
        #Tuples of letter counts will be the same
        #there will be a map - each tuple will be the key and the value will 
        #array of strings that match
        #go through each word and make a tuple for it 

        tupleMap = defaultdict(list)

        for currentWord in strs:
            countArr = [0]*26
            for letter in currentWord:
                letterIndex = ord(letter) - ord('a')
                countArr[letterIndex] += 1
            countArr = tuple(countArr)
            tupleMap[countArr].append(currentWord)
        
        result = list(tupleMap.values())

        return result

        