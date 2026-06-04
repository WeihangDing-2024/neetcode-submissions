class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        cnt = defaultdict(int)
        res = 0
        while j < len(s):
            cnt[s[j]] += 1
            if cnt[s[j]] >= 2:
                res = max(res, j-i)
                while s[i] != s[j]:
                    cnt[s[i]] -= 1
                    i += 1
                cnt[s[i]] -= 1
                i += 1
            j += 1
        res = max(res, j-i)
        return res



        