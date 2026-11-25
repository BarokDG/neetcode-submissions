class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        max_freq = 0
        freq = Counter(nums)

        for k, v in freq.items():
            if v > max_freq:
                max_freq = v
                majority = k
        
        return majority