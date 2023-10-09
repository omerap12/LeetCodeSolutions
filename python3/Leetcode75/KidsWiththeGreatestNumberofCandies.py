# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_child = max(candies)
        for child in candies:
            if child + extraCandies >= max_child:
                res.append[True]
            else:
                res.append[False]
        return res

candies = [4,2,1,1,2]
extraCandies = 1
n = Solution()
print(n.kidsWithCandies(candies,extraCandies))