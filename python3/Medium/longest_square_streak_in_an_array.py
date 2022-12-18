# https://leetcode.com/problems/longest-square-streak-in-an-array/description/
import math
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        We want to get for each number its longest sqrt subsequence.
        first we sort in descended order, to start with the largest value.
        then we convert the list to set
        then for each number we checked if its sqrt is in the set if so add 1 to counter and number to visited (to avoid
        iterating on him again)
        return the max counter.
        """
        nums.sort(reverse=True)
        set_nums = set(nums)
        res = 0
        visited = set()
        for number in nums:
            if number in visited:
                continue
            root = number
            tmp_counter = 0
            while root and root in set_nums:
                if root in visited:
                    break
                visited.add(root)
                root = math.sqrt(root)
                tmp_counter += 1
            res = max(res,tmp_counter)
        return res if res != 1 else -1



n = Solution()
nums = [4,3,6,16,8,9,81,2,6561] # 4
nums = [2,3,4,5,6,7]
nums = [1,1,1,1]
print(n.longestSquareStreak(nums))