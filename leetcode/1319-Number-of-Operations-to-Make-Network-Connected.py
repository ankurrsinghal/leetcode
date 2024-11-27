class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cn = len(connections)
        if cn < n - 1:
            return -1

        parent = [i for i in range(n)]
        ranks = [1] * n

        def find(n):
            p = n
            
            while p != parent[p]:
                p = parent[p]
                parent[p] = parent[parent[p]]

            return p
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            r1 = ranks[p1]
            r2 = ranks[p2]

            if r1 >= r2:
                parent[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parent[p1] = p2
                ranks[p2] += ranks[p1]
            
            return p1, p2

        wires_required = n - 1
        spare = 0
        for [n1,n2] in connections:
            p1,p2 = union(n1,n2)
            if p1 != p2: wires_required -= 1
            else: spare += 1


        return wires_required if wires_required <= spare else -1