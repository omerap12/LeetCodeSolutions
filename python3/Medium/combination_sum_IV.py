from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 0
        for number in nums:
            if number <= target:
                dp[number] += 1
        for i in range(1, target + 1, 1):
            tmp = sum(dp[i - num] for num in nums if i > num)
            dp[i] += tmp
        return dp[-1]
