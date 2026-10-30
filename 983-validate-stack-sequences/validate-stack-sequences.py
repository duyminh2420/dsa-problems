class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        idx = 0
        stack = []
        for x in pushed:
            #check the condition if the pop in this push match it with the pop in the index
            stack.append(x)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        return len(stack) == 0 