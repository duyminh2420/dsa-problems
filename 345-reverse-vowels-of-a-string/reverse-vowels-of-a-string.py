class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        low, high = 0, len(s) - 1
        while low < high:
            while low < high and s[low] not in "aeiouAEIOU": low += 1
            while low < high and s[high] not in "aeiouAEIOU": high -= 1
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return "".join(s)