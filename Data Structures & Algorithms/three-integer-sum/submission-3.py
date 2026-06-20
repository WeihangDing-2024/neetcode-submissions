class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif threeSum < 0:
                    j += 1
                else:
                    k -= 1
        return res
        