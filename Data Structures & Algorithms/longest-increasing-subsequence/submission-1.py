class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find(val):
            if not res:
                return 0
            low, high = 0, len(res)-1
            while low <= high:
                mid = (low + high) // 2
                mid_val = res[mid]
                if mid_val >= val:
                    high = mid - 1
                else:
                    low = mid + 1
            return low


        res = []
        for i in range(len(nums)):
            curr = nums[i]
            idx = find(curr)
            if idx >= len(res):
                res.append(curr)
            else:
                res[idx] = curr
        return len(res)
