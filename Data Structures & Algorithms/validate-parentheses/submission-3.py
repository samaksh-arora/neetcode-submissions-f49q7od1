class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       closingBrackets = { ')': '(', '}':'{', ']': '['}
       for b in s:
            if b in closingBrackets:
                if stack and stack[len(stack)-1] == closingBrackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
       if not stack:
            return True
       else:
            return False