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

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
