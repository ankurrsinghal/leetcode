class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.N = len(arr)
        self.tree = [ {} ] * (4 * len(arr) + 1)
        self.build(0, 0, len(arr) - 1, arr)

    def build(self, index, start, end, arr):
        if start == end:
            self.tree[index] = { arr[start]: 1 }
            return

        mid = (start + end) // 2
        left = 2 * index + 1
        right = 2 * index + 2
        self.build(left, start, mid, arr)
        self.build(right, mid + 1, end, arr)

        mapL = self.tree[left] 
        mapR = self.tree[right]

        merged_map = {}
        for key in set(mapL) | set(mapR):
            merged_map[key] = mapL.get(key, 0) + mapR.get(key, 0)
        
        self.tree[index] = merged_map

    def querySegmentTree(self, index, start, end, low, high, value):
        # no overlap ( start end low high ) ( low high start end )
        if end < low or start > high:
            return 0

        # complete overlap ( low start end high )
        if low <= start and end <= high:
            return self.tree[index].get(value, 0)

        # partial overlap ( low start high end ) ( start low end high )
        mid = (start + end) // 2
        left = self.querySegmentTree(2*index + 1, start, mid, low, high, value)
        right = self.querySegmentTree(2*index + 2, mid + 1, end, low, high, value)

        return left + right


    def query(self, left: int, right: int, value: int) -> int:
        return self.querySegmentTree(0, 0, self.N - 1, left, right, value)