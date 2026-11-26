class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    break
                
                nums[i], nums[j] = nums[j], nums[i]
                i = j

        return nums