# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_value,min_value = max(citations),0
        ret = None
        while min_value <= max_value:
            mid = (max_value + min_value) // 2
            if self.condition(citations,mid):
                ret = mid
                min_value = mid + 1
            else:
                max_value = mid - 1
        return ret
         

    def condition(self,citations: List[int],val:int) -> bool:
        counter = 0
        for c in citations:
            if c >= val:
                counter += 1
        return True if counter >= val else False

n = Solution()
citations = [3,0,6,1,5]
print(n.hIndex(citations=citations))
