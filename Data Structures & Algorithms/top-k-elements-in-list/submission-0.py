class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res_lst = []
        for key, value in cnt.items():
            res_lst.append([value, key])
        res_lst.sort(reverse = True)
        
        res = []
        for i in range(k):
            res.append(res_lst[i][1])
        return res
        