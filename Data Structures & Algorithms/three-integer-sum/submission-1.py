class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            
            while k > j:
                # print(i, j, k)
                # print(f"sum is {nums[i]+nums[j]+nums[k]}")
                if k-1 >= j and nums[k] == nums[k-1]:
                    k -= 1
                    continue
                if j+1 < k and nums[j] == nums[j+1]:
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    # print("now append")
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    continue
        return res