class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        hashMap2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashMap[s[i]] = 1 + hashMap.get(s[i],0)
            hashMap2[t[i]] = 1 + hashMap2.get(t[i],0)
        return hashMap == hashMap2




        
        