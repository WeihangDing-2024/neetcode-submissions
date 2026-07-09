class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        res_idx = [-1, -1]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j or (s[i] == s[j] and ((j-i) == 1 or dp[i+1][j-1])):
                    dp[i][j] = True
                    if j - i + 1 > res_len:
                        res_len = j - i + 1
                        res_idx = [i, j]
                # print(i, j)
                # print(dp)
        return s[res_idx[0]: res_idx[1]+1]
        