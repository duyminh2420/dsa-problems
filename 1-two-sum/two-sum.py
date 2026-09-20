class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {} #{nums[i]: i}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashset:
                return [hashset[diff], i]
            hashset[nums[i]] = i
