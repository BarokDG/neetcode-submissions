class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countN = {}

        for i in range(len(nums)):
            num = nums[i]

            diff = target - num

            if diff in countN:
               return [countN[diff], i]
                
            if num not in countN:
                countN[num] = i