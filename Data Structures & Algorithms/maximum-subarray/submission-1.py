class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')
        prev = 0
        for i in range(n):
            if prev < 0:
                prev = nums[i]
            else:
                prev = nums[i] + prev
            res = max(res, prev)
        return res