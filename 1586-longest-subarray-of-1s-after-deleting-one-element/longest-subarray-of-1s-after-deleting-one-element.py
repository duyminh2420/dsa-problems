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
            
            #then if the zeroCount is greater than 1 (we already reach the limit)
            #check the left if it is 0 we continue, reset the zero, move the next left
            #check if the left is is 1 we stop and move on next left
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            #keep expanding:
            res = max(res, right - left)
        return res
