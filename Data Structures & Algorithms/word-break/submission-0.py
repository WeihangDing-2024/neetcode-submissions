class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        wordSet = set(wordDict)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j+1] in wordSet:
                    dp[i][j] = True
                else:
                    for m in range(i, j):
                        if dp[i][m] and dp[m+1][j]:
                            dp[i][j] = True
        return dp[0][n-1]