class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        COLOR_1 = 0
        COLOR_2 = 1

        colors = [-1] * N

        def dfs(node):
            color = colors[node]

            if color == -1:
                colors[node] = COLOR_1

            opposite_color = COLOR_2 if colors[node] == COLOR_1 else COLOR_1

            for n in graph[node]:
                color_n = colors[n]
                if color_n == -1:
                    colors[n] = opposite_color
                    if not dfs(n):
                        return False
                elif color_n == colors[node]:
                    return False

            return True
        
        for i in range(N):
            if colors[i] == -1:
                if not dfs(i):
                    return False
        
        return True