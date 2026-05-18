class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums_set:
                continue
            curr = num
            curr_len = 0
            while curr in nums:
                curr += 1
                curr_len += 1
            res = max(res, curr_len)
        return res