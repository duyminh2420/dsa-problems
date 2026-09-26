class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        #using sliding window and have curr to keep track of number of 0 
        left = 0
        ans = 0
        curr = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
                