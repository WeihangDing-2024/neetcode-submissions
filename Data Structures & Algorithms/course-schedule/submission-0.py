class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for neighbor in adj_lst[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2
            return True
        
        # build graph
        ## adj list
        adj_lst = [[] for _ in range(numCourses)]
        for neighbor in prerequisites:
            start, end = neighbor[0], neighbor[1]
            adj_lst[start].append(end)
        
        # 0: not visited; 1: visiting; 2: visited
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        