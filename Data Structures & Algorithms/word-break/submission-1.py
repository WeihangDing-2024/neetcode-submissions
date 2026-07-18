class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = [False for _ in range(n)]

        if s[0] in wordSet:
            dp[0] = True

        for i in range(1, n):
            if s[:i+1] in wordSet:
                dp[i] = True
                continue
            for j in range(0, i):
                if dp[j] and s[j+1:i+1] in wordSet:
                    dp[i] = True
        return dp[-1]