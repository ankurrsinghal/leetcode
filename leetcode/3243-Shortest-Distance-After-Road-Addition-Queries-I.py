class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        distances = [501] * n
        distances[0] = 0

        for i in range(1, n):
            graph[i - 1].append(i)

        def findShortestPath(node):
            visited = [0] * n
            q = deque([node])
            visited[node] = 1
            while q:
                for _ in range(len(q)):
                    neighbour = q.popleft()
                    for adj in graph[neighbour]:
                        if visited[adj] == 0:
                            visited[adj] = 1
                            if distances[adj] > distances[neighbour] + 1: q.append(adj)
                            distances[adj] = min(distances[adj], distances[neighbour] + 1)
        
        findShortestPath(0)

        answer = [-1] * len(queries)

        for i, [n1, n2] in enumerate(queries):
            graph[n1].append(n2)
            findShortestPath(n1)
            answer[i] = distances[-1]

        return answer