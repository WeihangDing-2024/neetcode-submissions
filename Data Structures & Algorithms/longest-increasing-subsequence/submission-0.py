class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[-1] = 1

        # take i as start point, what's the LIS
        
        for i in range(len(nums)-2, -1, -1):
            local_res = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    local_res = max(local_res, 1 + dp[j])
            dp[i] = local_res
        return max(dp)