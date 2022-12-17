# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        We calculate for each zero index how much 1's are next to him and then remove the zero who has the most
        1's before and after him.
        We add 0 at the begiing of the array for input like 1,1,1,1,0,1,1,0 -> so we can add the 1's before the last 0
        """
        if nums[0] != 0:
            nums.insert(0,0)
        tmp = []
        counter = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                counter += 1
            else:
                tmp.append(counter)
                counter = 0
        tmp.reverse()
        if len(tmp) == 1:
            return sum(nums) - 1
        res = 0
        for i in range(1, len(tmp), 1):
            res = max(res, tmp[i - 1] + tmp[i])
        return res


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
# nums = [1, 1, 0, 1]
n = Solution()
print(n.longestSubarray(nums))
