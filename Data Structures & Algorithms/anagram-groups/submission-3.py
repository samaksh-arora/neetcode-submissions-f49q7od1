class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        anagramGroups = defaultdict(list)

        for word in strs:
            letterFrequencyCountArray = [0] * 26
            for letter in word:
                letterIdx = ord(letter) - ord('a')
                letterFrequencyCountArray[letterIdx] += 1

            letterFrequencyCountArray = tuple(letterFrequencyCountArray)
            anagramGroups[letterFrequencyCountArray].append(word)
        
        return list(anagramGroups.values())