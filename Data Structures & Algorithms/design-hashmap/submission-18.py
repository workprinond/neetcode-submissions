class MyHashMap:

    

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(1000)]
    
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        self.buckets[index] = [key, value] 
    
    def get(self, key: int) -> int:
        index = key % self.size
        if self.buckets[index] and self.buckets[index][0] == key:
            return self.buckets[index][1]
        return -1
    
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.buckets[index] and self.buckets[index][0] == key:
            self.buckets[index] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)