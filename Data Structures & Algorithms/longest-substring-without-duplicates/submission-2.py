class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        cnt = defaultdict(int)
        res = 0
        while j < len(s):
            cnt[s[j]] += 1
            while cnt[s[j]] >= 2:
                cnt[s[i]] -= 1
                i += 1
            res = max(res, j-i)
            j += 1
        return res



        