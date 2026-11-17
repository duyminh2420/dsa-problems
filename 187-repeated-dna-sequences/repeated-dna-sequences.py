class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        #substring sequences -> sliding window, with 10 letter long that occur more than 1 -> hashmap to store and check if it is more than 2, return it
        L = 10 
        n = len(s)
        seen = set()
        output = set()
        #iterate through all the seuqneces:
        for start in range(n - L + 1):
            tmp = s[start: start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return list(output)



