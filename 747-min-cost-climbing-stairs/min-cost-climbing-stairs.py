class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #climbing stairs - needs the previous steps to complete
        dp = [0] * (len(cost)+1)
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(cost)]