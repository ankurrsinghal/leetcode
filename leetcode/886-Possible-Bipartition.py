class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color_1 = 1
        color_2 = 2
        graph = defaultdict(list)
        for [s,d] in dislikes:
            graph[s-1].append(d-1)
            graph[d-1].append(s-1)

        colors = [-1] * n

        def dfs(node):
            
            if colors[node] == -1:
                colors[node] = color_1

            for x in graph[node]:
                if colors[x] == colors[node]:
                    return False
                if colors[x] == -1:
                    colors[x] = color_2 if colors[node] == color_1 else color_1
                    if not dfs(x):
                        return False
            
            return True

        for i in range(n):
            if colors[i] == -1:
                if not dfs(i):
                    return False
                
        return True