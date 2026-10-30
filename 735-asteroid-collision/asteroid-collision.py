class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        #maintain the stack and compare for the next stack, return stack
        stack = []
        ans = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                # negative asteroid destroys others in stack one by one
                while len(stack) > 0 and stack[-1] < abs(x):
                    stack.pop()
                # negative asteroid destroyed everyone    
                if len(stack) == 0:
                    ans.append(x)
                #negative
                else:
                    if stack[-1] == abs(x):
                        stack.pop()
        ans += stack
        return ans
