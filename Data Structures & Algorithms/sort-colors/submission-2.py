class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        
        for i in range(count[0]):
            nums[i] = 0
        
        start = count[0]
        end = start + count[1]
        for j in range(start, end):
            nums[j] = 1
        
        start = end
        end = start + count[2]
        for k in range(start, end):
            nums[k] = 2