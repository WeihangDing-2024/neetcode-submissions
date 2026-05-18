class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for key, values in cnt.items():
            if values >= 2:
                return True
        return False
        