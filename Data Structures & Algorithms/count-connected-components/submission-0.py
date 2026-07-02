class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, parent):
            if node in seen:
                return
            seen.add(node)
            for neighbor in adj_lst[node]:
                dfs(neighbor, node)
            return

        
        adj_lst = [[] for _ in range(n)]
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adj_lst[n1].append(n2)
            adj_lst[n2].append(n1)
        
        seen = set()
        res = 0
        
        for node in range(n):
            if node not in seen:
                res += 1
                dfs(node, None)
        return res        