class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        closingToOpeningBracketsMap = {')': '(', ']': '[', '}': '{'}

        stack = []

        for bracket in s:
            if bracket in closingToOpeningBracketsMap:
                if stack and stack[len(stack)-1]:
                    openingBracket = stack.pop()
                    if openingBracket != closingToOpeningBracketsMap[bracket]:
                        return False
                else:
                    return False
            else:  
                stack.append(bracket)
        
        if not stack:
            return True
        else:
            return False


#[{]
#[[]
#[(]