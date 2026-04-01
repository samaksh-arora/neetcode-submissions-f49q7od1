class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = {}
        freq2 = {}
        for letter in s:
            freq1[letter] = freq1.get(letter,0)+1
        for letter in t:
            freq2[letter] = freq2.get(letter,0)+1

        for key in freq1:
            if key not in freq2:
                return False
            if freq1[key] != freq2[key]:
                return False
        return True