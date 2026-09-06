class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            first_max = heapq.heappop_max(stones)
            second_max = heapq.heappop_max(stones)

            diff = first_max - second_max
            if diff > 0:
                heapq.heappush_max(stones, diff)
        
        remaining = 0 if len(stones) == 0 else stones[0]
        return remaining
