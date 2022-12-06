class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        L = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and L[i] < L[j] + 1:
                    L[i] = L[j] + 1
        
        return max(L)

