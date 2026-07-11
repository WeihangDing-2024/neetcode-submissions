class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [[float('-inf') for _ in range(m)] for _ in range(m)]


        res = float('-inf')
        for i in range(m-1, -1, -1):
            for j in range(i, m):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]
                res = max(res, dp[i][j])
        return res