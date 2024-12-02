class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.prefixSum = [0] * N
        self.prefixSum[0] = nums[0]

        for i in range(1, N):
            self.prefixSum[i] += self.prefixSum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        sumTotal = self.prefixSum[right]
        if left == 0:
            return sumTotal

        sumLeft = self.prefixSum[left - 1]
        
        return sumTotal - sumLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)