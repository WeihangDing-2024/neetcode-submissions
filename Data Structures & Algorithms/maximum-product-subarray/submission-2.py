class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prevMax = 1
        prevMin = 1
        res = float('-inf')
        for num in nums:
            curMax = max(num, prevMax * num, prevMin * num)
            curMin = min(num, prevMax * num, prevMin * num)
            prevMax = curMax
            prevMin = curMin
            res = max(res, prevMax)
            # print(f'num is {num}, prevMax is {prevMax}, prevMin is {prevMin}')
        return res























