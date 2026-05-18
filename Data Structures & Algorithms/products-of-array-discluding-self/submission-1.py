class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            suffix_product[j] = suffix_product[j+1] * nums[j+1]
        res = []
        for k in range(0, len(nums)):
            res.append(prefix_product[k] * suffix_product[k])
        return res