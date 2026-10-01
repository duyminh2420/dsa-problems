class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char in closeToOpen:
                if stack and closeToOpen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False 



