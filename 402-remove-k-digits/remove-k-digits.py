class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Google
        #Mono stack 
        numStack = []
        #Construct a monotone increasing sequence of digits:
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        #Trunk the remaining k digit at the end 
        #In the case k == 0 return the entire list 
        finalStack = numStack[:-k] if k else numStack
        #trip the leading zeros:
        return "".join(finalStack).lstrip('0') or "0"