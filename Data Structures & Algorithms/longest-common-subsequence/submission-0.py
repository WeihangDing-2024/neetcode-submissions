class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # Create a (m+1) x (n+1) matrix filled with 0s
        # The extra row and col handle the base cases (empty strings)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Start iterating from 1 to m and 1 to n
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Remember we need to offset the text indices by -1 
                # because our dp array is 1-indexed relative to the strings
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]