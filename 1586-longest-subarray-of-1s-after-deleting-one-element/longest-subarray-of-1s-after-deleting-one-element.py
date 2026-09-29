class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        #size of the longest non empty subarray containing only 1's in array
        zeroCount = 0
        left = 0
        res = 0
        #start from the right pointer:
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            
            # We are allowed to have at most one 0 in the window,
            # because that 0 can be deleted.
            # If we have more than one 0, shrink from the left
            # until only one 0 remains.
            while zeroCount > 1:
                # If the element leaving the window is a 0,
                # decrease the zero count.
                if nums[left] == 0:
                    zeroCount -= 1
                #move the next left boundaries 
                left += 1

            # The window is now valid and contains at most one 0.
            # We delete that one 0, so the answer is window size - 1.
            res = max(res, right - left)
        return res
