class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = [0]

        def dfs(i, j, connected):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == "#":
                return
            if grid[i][j] == "1":
                grid[i][j] = "#"
                if not connected:
                    res[0] += 1
                dfs(i+1, j, True)
                dfs(i-1, j, True)
                dfs(i, j+1, True)
                dfs(i, j-1, True)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j, False)
        return res[0]

            
                    
        