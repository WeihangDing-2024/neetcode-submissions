class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i, num in enumerate(nums):
            if i == 0 or i == 1:
                continue
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]
        