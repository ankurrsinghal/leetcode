class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for [src, dest] in invocations:
            graph[src].append(dest)
        
        visited = [-1] * n
        def dfs(node):
            
            visited[node] = 0

            for n in graph[node]:
                if visited[n] == -1:
                    dfs(n)
            
            visited[node] = 1
        
        dfs(k)

        canBeRemoved = True
        for [src, dest] in invocations:
            if visited[src] != 1:
                if visited[dest] == 1:
                    canBeRemoved = False
                    break

        return [i for i in range(n) if not canBeRemoved or visited[i] != 1]