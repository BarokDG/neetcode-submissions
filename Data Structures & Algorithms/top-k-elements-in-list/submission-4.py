class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequencies
        # put the frequencies in the bucket
        # while output is less than k, pop from buckets from right to left and add numbers
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums))]

        for key, v in freq.items():
            buckets[v - 1].append(key)
        
        out = []
        for i in range(len(buckets) - 1, -1, -1):
            while buckets[i]:
                out.append(buckets[i].pop())

                if len(out) >= k:
                    return out
            
