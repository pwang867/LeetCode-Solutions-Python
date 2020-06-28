# # use dummy head and dummy tail to ease implementation
# hashmap + doubly linked list


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = ListNode(0, 0)    # use dummy head and dummy tail to ease implementation
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}                 # {key: ListNode}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        node = self.map[key]
        self._shift_node_to_tail(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            node = self.map[key]
            self._shift_node_to_tail(node)
            node.value = value
        else:
            if len(self.map) == self.capacity:
                oldest = self.head.next
                self._remove_node(oldest)
                del self.map[oldest.key]
            new_node = ListNode(key, value)
            self.map[key] = new_node
            self._add_node_to_tail(new_node)

    def _shift_node_to_tail(self, node):
        self._remove_node(node)
        self._add_node_to_tail(node)

    def _remove_node(self, node):
        # remove from doubly linked list only, not the map
        if not node or not self.map or not node.next or not node.prev:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _add_node_to_tail(self, node):
        if not node:
            return
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        node.prev.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# collections.OrderedDict() is implemented by double linked-list
# it can search, delete in O(1) time, and will keep added items in order


import collections
class LRUCache1(object):

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
                self.cache.popitem(last=False)     # dict.popitem(last=False)
        
        self.cache[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following 
operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

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
