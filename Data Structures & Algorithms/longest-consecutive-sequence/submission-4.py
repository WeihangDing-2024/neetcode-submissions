class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums:
            if num+1 in nums_set:
                continue
            curr_len = 1
            curr_num = num
            while curr_num - 1 in nums_set:
                curr_len += 1
                curr_num -= 1
            res = max(res, curr_len)
        return res