class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._nums = sorted(nums)
        self._k = k
        

    def add(self, val: int) -> int:
        index = self.find_insert_index(val)

        self._nums.insert(index, val)

        return self._nums[-self._k]

    def find_insert_index(self, val:int) -> int:
        l, r = 0, len(self._nums)
        
        while l < r:
            mid = (l + r) // 2

            if self._nums[mid] < val:
                l = mid + 1
            else:
                r = mid
            
        return l