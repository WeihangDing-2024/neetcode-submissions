class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bSearch(num):
            low, high = 0, len(seq) - 1
            while low <= high:
                mid = (low + high) // 2
                if seq[mid] < num:
                    low = mid + 1
                else:
                    high = mid - 1
            return low        
        
        seq = []
        for num in nums:
            idx = bSearch(num)
            if idx >= len(seq):
                seq.append(num)
            else:
                seq[idx] = num
            # print(idx, seq)
        return len(seq)
        