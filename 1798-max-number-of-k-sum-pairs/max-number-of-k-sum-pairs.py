class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #using the l, r to point to the same number as target from both side, if it is less than target I will move down, looks like binary search 
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            mid = nums[l] + nums[r]
            if mid == k:
                res += 1
                l += 1
                r -= 1
            elif mid < k:
                l += 1
            else:
                r -= 1
        return res
