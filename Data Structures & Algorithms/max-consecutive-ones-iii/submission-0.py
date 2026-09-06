class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_c = 0
        temp_k = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                temp_k += 1

            while temp_k > k:
                if nums[l] == 0:
                    temp_k -= 1
                l += 1
            
            max_c = max(max_c, r - l + 1)

        return max_c