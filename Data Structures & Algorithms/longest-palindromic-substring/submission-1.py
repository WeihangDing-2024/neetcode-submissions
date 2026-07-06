class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] means s[i:j] is a palindrome
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == None:
                    if j == i or (j == i+1 and s[j] == s[i]):
                        dp[i][j] = True
                        offset = 1
                        while i-offset >= 0 and j+offset < len(s) and s[i-offset] == s[j+offset]:
                            dp[i-offset][j+offset] = True
                            offset += 1
                        while i-offset >= 0 and j+offset < len(s):
                            dp[i-offset][j+offset] = False
                            offset += 1
                    else:
                        dp[i][j] = False
        # print(dp)
        res_len = 1
        res_idx = [0, 1]

        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] and j+1-i > res_len:
                    res_idx = [i, j+1]
                    res_len = j+1-i
        return s[res_idx[0]:res_idx[1]]
                        
