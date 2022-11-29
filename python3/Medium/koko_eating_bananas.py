import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        max_banana_pile = max(piles)
        if h == len(piles):
            return max_banana_pile
        # binary search
        min_banana_pile = 1
        min_banana_current = max_banana_pile
        while min_banana_pile < max_banana_pile:
            mid = (max_banana_pile + min_banana_pile) // 2
            if self.check_banana_per_hour(mid, piles, h):
                min_banana_current = mid
                max_banana_pile = mid
            else:
                min_banana_pile = mid + 1
        return min_banana_current

    def check_banana_per_hour(self, bph, piles, h):
        banana_counter = 0
        for number in piles:
            banana_counter += math.ceil(number / bph)
        if banana_counter <= h:
            return True
        return False
