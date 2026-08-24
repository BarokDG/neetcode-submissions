class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = set(nums)

        longest = 0
        for num in record:
            if (num - 1) in record:
                continue
            
            count = 0
            curr = num
            while curr in record:
                count += 1
                curr += 1
            
            longest = max(longest, count)

        return longest
