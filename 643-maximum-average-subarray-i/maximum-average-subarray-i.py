class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        #continuous subarray -> window -> sliding window 
        #we find the maximum of the window of 4 (from i to i + k), then return it by divide k later 
        # window = sum(nums[:k])
        # maxWindow = window 
        # for r in range(k, len(nums)):
        #     window += nums[r]
        #     window -= nums[r-k]
        #     maxWindow = max(maxWindow, window)
        # return maxWindow / k



        curr = 0
        for i in range(k):
            curr += nums[i]
        ans = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            ans = max(ans, curr)
        return ans/k




        #continuous subarray -> window -> sliding window 
        # window = sum(nums[:k])
        # maxWindow = window
        # for r in range(k, len(nums)):
        #     window += nums[r]
        #     window -= nums[r-k]
        #     maxWindow = max(maxWindow, window)
        # return maxWindow / k