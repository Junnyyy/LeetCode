from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cur = 0

        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            maxSum = max(cur, maxSum)
        
        return maxSum
        
