class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        #Google problem
        #this questions is 2D array, we can use dfs for the moving down as (m-1)(n-1)
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False 
        @cache
        def dp(r, c, cur):
            if r >= m or c >= n:
                return False
            cur += (grid[r][c]*2 - 1)
            if r == m - 1 and c == n - 1:
                return cur == 0
            return dp(r + 1, c, cur) or dp(r, c + 1, cur)

        return dp(0, 0, 0)