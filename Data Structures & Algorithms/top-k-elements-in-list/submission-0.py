class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        count_sorted = sorted(count.items(), key=lambda x: x[1])
        return [x[0] for x in count_sorted[-k:]]