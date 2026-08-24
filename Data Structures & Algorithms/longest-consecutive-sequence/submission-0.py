class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = {}

        for num in nums:
            record[num] = 1

        max_count = 0
        for key in record:
            if (key - 1) in record:
                continue
            
            count = 1
            temp_key = key + 1
            while temp_key in record:
                count += 1
                temp_key += 1
            
            max_count = max(max_count, count)

        return max_count
