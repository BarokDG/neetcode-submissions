class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicates = set()

        for num in nums:
            if num in duplicates:
                return num

            duplicates.add(num)