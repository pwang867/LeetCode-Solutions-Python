# collections.OrderedDict() is implemented by double linked-list
# it can search, delete in O(1) time, and will keep added items in order
import collections
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            val = self.cache.pop(key)  # move the key to the end of OrderedDict
            self.cache[key] = val
            return val      

    def put(self, key, value):
        
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) >= self.capacity:
                for x in self.cache:
                    self.cache.pop(x)
                    break  # only remove the oldest key
        
        self.cache[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
