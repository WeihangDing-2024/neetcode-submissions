class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, curr, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            for i in range(start, len(candidates)):
                val = candidates[i]
                if val > target:
                    break
                curr.append(val)
                dfs(i, curr, target - val)
                curr.pop()

        dfs(0, [], target)
        return res