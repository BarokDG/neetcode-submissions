class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = 0
        duplicates = set()

        for num in nums:
            if num in duplicates:
                d = num
                break

            duplicates.add(num)
        
        return d