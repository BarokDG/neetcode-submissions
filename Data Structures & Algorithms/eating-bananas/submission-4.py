class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            mid = (l + r) // 2
            
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / mid)

            if hours_needed <= h:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_speed
            
