class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        #combination sum3 using backtracking
        res = []
        def backtrack(remain, comb, next_start): #want to keep the combination, then the remain number, then track the next start to do it.
            if remain == 0 and len(comb) == k: #reaching max, basecase 
                res.append(list(comb))
                return 
            elif remain < 0 or len(comb) == k:
                return 
            
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain - i - 1, comb, i + 1)
                comb.pop()
        backtrack(n, [], 0)
        return res
            
