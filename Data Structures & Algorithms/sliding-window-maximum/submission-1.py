class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        d = deque()

        l = r = 0
        while r < len(nums):
            curr = nums[r]
            while d and d[-1] < curr:
                d.pop()
            d.append(curr)

            r += 1
            if r < k:
                continue

            out.append(d[0])
            if nums[l] == d[0]:
                d.popleft()
            l += 1

        return out