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

        for t in self._store[key].keys():
            if t < timestamp:
                v = self._store[key][t]

        return v
