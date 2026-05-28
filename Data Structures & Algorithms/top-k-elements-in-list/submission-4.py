class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = Counter(nums)

        freq_lst = [[] for _ in range(len(nums) + 1)]
        for num, freq in cnt.items():
            freq_lst[freq].append(num)
                
        res = []
        for i in range(len(freq_lst)-1, -1, -1):
            if freq_lst[i]:
                for num in freq_lst[i]:
                    res.append(num)
                    k -= 1
            if k <= 0:
                break
        
        return res
