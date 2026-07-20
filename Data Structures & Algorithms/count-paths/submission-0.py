class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1 for _ in range(n)]
        dp = [0 for _ in range(n)]
        for i in range(1, m):
            # print(prev)
            for j in range(n):
                if j == 0:
                    dp[j] = prev[j]
                else:
                    dp[j] = prev[j] + dp[j-1]
            prev = dp
        # print(prev)
        
        return prev[-1]
            