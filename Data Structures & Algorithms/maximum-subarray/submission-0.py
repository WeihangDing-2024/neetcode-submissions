class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        res = 0
        curr = 0
        for i, num in enumerate(nums):
            if curr + num < 0:
                curr = 0
            else:
                if curr + num >= res:
                    res = curr + num
                curr += num
        return res



        