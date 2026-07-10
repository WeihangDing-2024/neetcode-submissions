class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+2)]
        dp[n+1] = 1
        dp[n] = 1

        for i in range(n-1, -1, -1):
            num = int(s[i])
            if num == 0:
                continue
            if num > 2:
                if i < n-1:
                    dp[i] = dp[i+1]
                else:
                    dp[i] = 1
            else:
                if i < n-1:
                    if int(s[i:i+2]) <= 26:
                        dp[i] = dp[i+2] + dp[i+1]
                    else:
                        dp[i] = dp[i+1]
                else:
                    dp[i] = 1
        return dp[0]