class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        char_set = set()
        res = 0
        while j < len(s):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            res = max(res, j-i+1)
            j += 1
        return res