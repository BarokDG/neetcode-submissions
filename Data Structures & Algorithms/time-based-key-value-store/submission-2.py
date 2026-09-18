class TimeMap:
    def __init__(self):
        self._store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._store:
            self._store[key][timestamp] = value
            return

        self._store[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ""

        v = self._store[key].get(timestamp, "")
        if v:
            return v

        available_timestamps = list(self._store[key].keys())
        l, r = 0, len(available_timestamps) - 1
        while l <= r:
            mid = (l + r) // 2

            curr_timestamp = available_timestamps[mid]
            if curr_timestamp < timestamp:
                v = self._store[key][curr_timestamp]
                l = mid + 1
            else:
                r = mid - 1

        return v
