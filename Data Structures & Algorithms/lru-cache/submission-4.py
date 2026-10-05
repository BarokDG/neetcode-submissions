class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = collections.deque([])
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        (value, access_count) = self.cache[key]
        self.cache[key] = (value, access_count + 1)
        self.q.append(key)

        return value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = (value, 1)
        else:
            (_, access_count) = self.cache[key]
            self.cache[key] = (value, access_count + 1)
        
        self.q.append(key)

        while len(self.cache) > self.capacity:
            k = self.q.popleft()
            (v, count) = self.cache[k]
            count -= 1
            self.cache[k] = (v, count)
            if count == 0:
                self.cache.pop(k)
        

        
