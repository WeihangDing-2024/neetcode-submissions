class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = [1 for _ in range(len(nums))]
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res
        
        