class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = nums[0]
        for i in range(1, len(nums)):
            n = n ^ nums[i]
        for i in range(len(nums)+1):
            n = n ^ i
        return n
        