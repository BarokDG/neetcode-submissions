class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        d = deque()

        for i in range(k):
            curr = nums[i]
            while d and d[-1] < curr:
                d.pop()
            
            d.append(curr)
        
        out.append(d[0])

        for i in range(k, len(nums)):
            num_to_remove = nums[i - k]

            if num_to_remove == d[0]:
                d.popleft()

            curr = nums[i]
            while d and d[-1] < curr:
                d.pop()

            d.append(curr)
            out.append(d[0])

        return out