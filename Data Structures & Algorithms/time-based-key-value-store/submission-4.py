from collections import defaultdict

class TimeMap:
    def __init__(self):
        self._store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ""

        res = ""

        values = self._store[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2

            curr_timestamp = values[mid][0]
            if curr_timestamp == timestamp:
                return values[mid][1]
            elif curr_timestamp < timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
