class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. find the min value
        pivot = nums[0]
        if pivot == target:
            return 0

        found_min = False
        if nums[0] <= nums[-1]:
            min_index = 0
            found_min = True
        else:
            low, high = 0, len(nums) - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > pivot:
                    low = mid + 1
                elif nums[mid] < pivot:
                    high = mid
                else:
                    min_index = high
                    found_min = True
                    break
            if not found_min:
                min_index = low
        # print("min index, min val: ", min_index, nums[min_index])
        if nums[min_index] == target:
            return min_index

        # 2. check if the target is on the right of the max value
        # or on the left of the max value
        if pivot > target:
            low, high = (min_index + 1 + len(nums)) % len(nums), len(nums) - 1
        if pivot < target:
            low, high = 0, (min_index - 1 + len(nums)) % len(nums)
        # print(f"low, high is {low}, {high}")

        # 3. find the index of the target (or target does not exist)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            if nums[mid] < target:
                low = mid + 1
        return -1