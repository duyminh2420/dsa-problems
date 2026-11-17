class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        L = 10 
        n = len(s)
        seen = set()
        res = set ()
        for i in range(n - L + 1):
            if s[i: i + L] in seen:
                res.add(s[i: i + L])
            seen.add(s[i: i + L])
        return list(res)


