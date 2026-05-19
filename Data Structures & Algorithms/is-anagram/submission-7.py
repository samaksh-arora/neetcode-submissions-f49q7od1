class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = s
        string2 = t

        if len(string1) != len(string2):
            return False 

        string1FrequencyMap = {}
        string2FrequencyMap = {}

        for letter in string1:
            string1FrequencyMap[letter] = string1FrequencyMap.get(letter, 0) + 1
        
        for letter in string2:
            string2FrequencyMap[letter] = string2FrequencyMap.get(letter, 0) + 1
        
        return string1FrequencyMap == string2FrequencyMap