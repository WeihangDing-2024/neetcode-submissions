class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        res = 0
        for char in char_set:
            remain_k = k
            i, j = 0, 0
            while j < len(s):
                if s[j] != char and remain_k > 0:
                    remain_k -= 1
                elif s[j] != char and remain_k <= 0:
                    while remain_k <= 0:
                        if s[i] != char:
                            remain_k += 1
                        i += 1
                    remain_k -= 1
                res = max(res, j - i + 1)
                j += 1
        return res
