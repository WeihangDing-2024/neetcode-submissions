class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        # res_lst = []
        # for key, value in cnt.items():
        #     res_lst.append([value, key])
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in cnt.items():
            freq[value].append(key)
        # print(freq)

        res = []
        for i in range(len(freq)-1, -1, -1):
            if freq[i]:
                res += freq[i]
                k -= len(freq[i])
            if k <= 0:
                break
        return res
        
        # res = []
        # for i in range(k):
        #     res.append(res_lst[i][1])
        # return res
        return [0]