class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        visited = set()
        for num in nums_set:
            if num in visited:
                continue
            curr = num
            curr_len = 1
            while curr + 1 in nums_set:
                curr_len += 1
                curr += 1
                visited.add(curr)
            res = max(res, curr_len)
        return res
        