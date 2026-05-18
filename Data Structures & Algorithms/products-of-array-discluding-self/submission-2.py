class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # calculate the prefix array (product of all the elements before given index)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        # calculate the suffix array (product of all the elements after given index)
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        # calculate the result
        res = [1] * len(nums)
        for k in range(0, len(nums)):
            res[k] = prefix[k] * suffix[k]
        return res

        # prefix = [1, -1, 0, 0, 0]
        # suffix = [0, 6, 6, 3, 1]

        