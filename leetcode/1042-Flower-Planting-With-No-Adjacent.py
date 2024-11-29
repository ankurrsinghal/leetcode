class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        answer = [-1] * n
        
        graph = defaultdict(list)
        for u, v in paths:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        
        for node in range(n):
            used = set()

            for n in graph[node]:
                if answer[n] != -1:
                    used.add(answer[n])
            
            for color in range(1, 5):
                if not color in used:
                    answer[node] = color
                    break

        return answer
