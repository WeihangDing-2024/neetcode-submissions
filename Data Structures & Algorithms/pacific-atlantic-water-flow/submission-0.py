class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if adj to an ocean, return directly
        # if adj to a cell that can flow to both ocean, return
        m = len(heights)
        n = len(heights[0])

        # 2: not decided 1: true 0: false
        pacific = [[2 for _ in range(n)] for _ in range(m)]
        atlantic = [[2 for _ in range(n)] for _ in range(m)]

        def dfs(i, j, prev_h, arr):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if arr[i][j] == 1:
                return
            
            curr_h = heights[i][j]
            if curr_h >= prev_h:
                arr[i][j] = 1
                dfs(i+1, j, curr_h, arr)
                dfs(i-1, j, curr_h, arr)
                dfs(i, j+1, curr_h, arr)
                dfs(i, j-1, curr_h, arr)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dfs(i, j, 0, pacific)
                if i == m - 1 or j == n - 1:
                    dfs(i, j, 0, atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    res.append([i, j])
        return res
                    