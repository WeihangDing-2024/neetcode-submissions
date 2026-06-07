class Solution:
    def findMin(self, nums: List[int]) -> int:
        # not rotated
        if nums[0] < nums[-1]:
            return nums[0]
        if len(nums) == 1:
            return nums[0]
        
        # rotated
        low, high = 0, len(nums) - 1
        pivot = nums[0]
        while low < high:
            mid = (high + low) // 2
            mid_val = nums[mid]
            if mid_val >= pivot:
                low = mid + 1
            else:
                high = mid
        return nums[high]
