class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        out = []
        d = deque()

        l = 0
        for r in range(len(nums)):
            curr = nums[r]
            while d and d[-1] < curr:
                d.pop()
            d.append(curr)

            if r < k - 1:
                continue

            out.append(d[0])

            if nums[l] == d[0]:
                d.popleft()

            l += 1

        return out