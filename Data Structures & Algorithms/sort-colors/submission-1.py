class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        
        for i in range(count[0]):
            nums[i] = 0
        
        for j in range(count[0], count[0] + count[1]):
            nums[j] = 1
        
        for k in range(count[0] + count[1], count[0] + count[1] + count[2]):
            nums[k] = 2