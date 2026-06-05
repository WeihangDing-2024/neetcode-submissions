class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set(s)
        for char in char_set:
            i = 0
            for j in range(len(s)):
                if s[j] != char:
                    while k <= 0:
                        if i < len(s) and s[i] != char:
                            k += 1
                        i += 1
                        if i >= len(s):
                            break
                    k -= 1
                res = max(res, j - i + 1)
        return res
