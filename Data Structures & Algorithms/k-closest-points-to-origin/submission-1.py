class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(min_heap, (distance, [x, y]))

        res = []
        while len(res) < k:
            point = heapq.heappop(min_heap)
            res.append(point[1])

        return res