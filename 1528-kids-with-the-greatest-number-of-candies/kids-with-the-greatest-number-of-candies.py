class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)
        return result