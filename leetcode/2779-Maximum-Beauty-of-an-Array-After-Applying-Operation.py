class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        max_counter = 0
        j = 0
        for i in range(N):
            
            if j == N:
                return max_counter

            while j < N and nums[j] - nums[i] <= 2*k:
                j += 1                

            beauty = j - i
            max_counter = max(max_counter, beauty)

        return max_counter