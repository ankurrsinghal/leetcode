class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        visited = [-1] * N

        def dfs(node):
            visited[node] = 1

            for x in rooms[node]:
                if visited[x] == -1: dfs(x)
        
        dfs(0)
        
        return reduce(lambda x,y: x == 1 and y == 1, visited)