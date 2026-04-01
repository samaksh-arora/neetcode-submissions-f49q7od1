import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        nums = [0,1,2,3,4,5,6,7,8,9]
        s = ' '.join(s)
        l = 0
        r = len(s) - 1
        while (l < r):
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True    
            
