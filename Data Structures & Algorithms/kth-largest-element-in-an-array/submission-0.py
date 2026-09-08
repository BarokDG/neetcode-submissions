class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
                continue

            new = max(num, heapq.heappop(h))
            heapq.heappush(h, new)

        return h[0]