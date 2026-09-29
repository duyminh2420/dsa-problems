class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        #window expanding until invalid (2 zeros)
        left = 0
        res = 0
        zeroCount = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            res = max(res, right - left)
        return res
