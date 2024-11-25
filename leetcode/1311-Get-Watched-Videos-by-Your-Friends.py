class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        N = len(friends)

        q = deque([id])
        k = 0
        visited = [-1] * N
        visited[id] = 1
        friendsAtLevel = []
        while q:
            if k == level:
                friendsAtLevel = list(q)
                break
            for _ in range(len(q)):
                node = q.popleft()
                for x in friends[node]:
                    if visited[x] == -1:
                        q.append(x)
                        visited[x] = 1
            k += 1
        
        result = {}
        for friend in friendsAtLevel:
            for video in watchedVideos[friend]:
                result[video] = result.get(video, 0) + 1

        answer = []
        for video, count in result.items():
            answer.append((count, video))
        
        answer.sort()

        return [ x[1] for x in answer ]