class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # the highest wall before this index
        prefix = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix[i] = max(prefix[i-1], height[i-1])

        # the highest wall after this index
        suffix = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        res = 0
        for i in range(0, len(height)):
            max_m, max_n = prefix[i], suffix[i]
            if max_m > height[i] and max_n > height[i]:
                res += min(max_m, max_n) - height[i]
            # print(res)
        return res
        