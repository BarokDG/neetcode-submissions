class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for (x, y) in points:
            distance = math.sqrt((x ** 2 + y ** 2))
            
            if len(h) < k:
                heapq.heappush_max(h, (distance, x, y))
                continue
            
            if distance < h[0][0]:
                heapq.heappop_max(h)
                heapq.heappush_max(h, (distance, x, y))

        res = []
        while h:
            (d, x, y) = heapq.heappop_max(h)
            res.append([x, y])
        
        return res