class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_res = []
        candidates.sort()

        def combination(res_arr, curr_sum, j):
            if curr_sum == target:
                final_res.append(res_arr.copy())
                return 
            if curr_sum > target:
                return
            for i in range(j, len(candidates)):
                res_arr.append(candidates[i])
                curr_sum += candidates[i]
                combination(res_arr, curr_sum, i)
                res_arr.pop()
                curr_sum -= candidates[i]
        
        combination([], 0, 0)
        return final_res

        