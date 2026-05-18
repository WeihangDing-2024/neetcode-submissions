class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = defaultdict(int) # key: num to find, value: original index
        for i in range(0, len(nums)):
            if nums[i] in num_map:
                return [num_map[nums[i]], i]
            num_map[target - nums[i]] = i
        return [-1, -1]
        