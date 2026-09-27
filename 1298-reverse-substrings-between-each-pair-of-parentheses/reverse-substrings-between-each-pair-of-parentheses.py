class Solution:
    def reverseParentheses(self, s: str) -> str:
        #reverse the string, and skip the brackets 
        #start with the empty string
        stack = [""]
        for c in s:
            #When we see '(', start a new level
            #This new string will contain everything inside the parentheses
            if c == "(":
                stack.append("")
            # When we see ')', we finished the current parentheses
            elif c == ")":
                # Get the string inside the parentheses
                curr = stack.pop()
                # Reverse it, then add it to the previous level
                stack[-1] += curr[::-1]
            else:
                # Regular letter: add it to the current level
                stack[-1] += c
        # The bottom of the stack contains the final answer
        return stack[0]