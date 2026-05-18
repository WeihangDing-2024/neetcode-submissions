class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for key, val in cnt.items():
            if val >= 2:
                return True
        return False
        