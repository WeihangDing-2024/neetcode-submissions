class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
                return nums[0]

        low, high = 0, len(nums) - 1
        pivot = nums[0]
        while low < high:
            mid = (high - low) // 2 + low
            if nums[mid] > pivot:
                low = mid + 1
            elif nums[mid] < pivot:
                high = mid
            else:
                return nums[high]
        return nums[high]
 