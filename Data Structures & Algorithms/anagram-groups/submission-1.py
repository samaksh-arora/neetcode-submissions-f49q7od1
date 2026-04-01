class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newMap = defaultdict(list)
        for i in strs:
            sortedS = ''.join(sorted(i))
            newMap[sortedS].append(i)
        return list(newMap.values())
            
