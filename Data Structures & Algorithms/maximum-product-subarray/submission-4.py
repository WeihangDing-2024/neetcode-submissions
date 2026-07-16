class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        prev_max = nums[0]
        prev_min = nums[0]
        for i in range(1, len(nums)):
            temp = prev_max
            prev_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            prev_min = min(nums[i], temp * nums[i], prev_min * nums[i])
            res = max(res, prev_max)
        return res