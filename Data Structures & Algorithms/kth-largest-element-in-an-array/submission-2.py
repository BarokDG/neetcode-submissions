class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
                continue

            if h[0] > num:
                continue

            heapq.heappushpop(h, num)

        return h[0]