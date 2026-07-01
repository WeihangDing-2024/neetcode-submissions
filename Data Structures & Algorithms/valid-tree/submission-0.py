class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, prev):
            if state[node] == 2:
                return True
            if state[node] == 1:
                return False
            state[node] = 1
            for neighbor in adj_lst[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            state[node] = 2
            return True
        
        # asyclic; connected

        # 0: unvisited 1: visiting 2: visited
        state = [0 for _ in range(n)]
        adj_lst = [[] for _ in range(n)]
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adj_lst[n1].append(n2)
            adj_lst[n2].append(n1)
        print(adj_lst)
        if not dfs(0, None):
            return False
        
        for val in state:
            if val != 2:
                return False
        return True