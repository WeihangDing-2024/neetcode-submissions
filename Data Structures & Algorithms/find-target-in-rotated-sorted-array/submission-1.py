class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid

            if mid_val >= nums[low]:
                if target >= nums[low] and target < mid_val:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > mid_val and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1