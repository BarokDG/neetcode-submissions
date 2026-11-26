class MyHashSet:

    def __init__(self):
        self.hash_set = {}

    def add(self, key: int) -> None:
        self.hash_set[key] = 1

    def remove(self, key: int) -> None:
        print(self.hash_set)
        self.hash_set.pop(key, None)
        
    def contains(self, key: int) -> bool:
        return key in self.hash_set
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)