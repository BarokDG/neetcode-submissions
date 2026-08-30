class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while r >= l:
            m = (l + r) // 2

            curr = nums[m]
            if target == curr:
                return m
            elif target > curr:
                l = m + 1
            else:
                r = m - 1
            
        return -1