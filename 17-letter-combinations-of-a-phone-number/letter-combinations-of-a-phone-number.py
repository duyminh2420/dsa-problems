class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        #return all letter combination -> backtracking 
        #create the map for each number:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        if len(digits) == 0:
            return []
        def backtracking(index, path): #what I need to save: current comb, next letter
            #if the path is the same length as digits, we have a complete combination:
            if len(path) == len(digits):
                res.append("".join(path))
                return
            # no edgecase 
            # base case
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                #move to the next letter
                backtracking(index + 1, path)
                #back track by removing the letter before moving onto the next one
                path.pop()
        backtracking(0, [])
        return res