# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        max_child = max(candies)
        for child in candies:
            if child + extraCandies >= max_child:
                ret.append(True)
            else:
                ret.append(False)
        return ret