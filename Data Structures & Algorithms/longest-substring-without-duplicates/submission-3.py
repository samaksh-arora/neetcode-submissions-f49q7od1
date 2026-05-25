class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #{z }
        #{z,x }
        #{z,x,y }
        #{y,z,x }
        #         v
        #[z,x,y,z,x,y,z]
        #   ^       

        if not s:
            return 0
        charSet = set()
        leftPtr = rightPtr = 0
        result = 1
        for i in range(len(s)):
            if s[rightPtr] in charSet:
                while s[leftPtr] != s[rightPtr]:
                    charSet.remove(s[leftPtr])
                    leftPtr+=1
                charSet.remove(s[leftPtr])
                leftPtr+=1
                charSet.add(s[rightPtr])
                result = max(result, len(charSet))
            else: 
                charSet.add(s[rightPtr])
                result = max(result, len(charSet))
            
            rightPtr += 1
            print(result, charSet)
        return result







