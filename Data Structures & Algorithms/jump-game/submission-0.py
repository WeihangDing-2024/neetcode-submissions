class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = nums[0]
        for i in range(1, len(nums)):
            if i > farest:
                return False
            farest = max(farest, i + nums[i])
            if farest >= len(nums) - 1:
                return True
        return True