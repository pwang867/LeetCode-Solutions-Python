# use structure of {freq: LFU} to implement LFU


class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1


class LRU:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node_to_tail(self, node):
        left, right = self.tail.prev, self.tail
        left.next = node
        node.prev = left
        node.next = right
        right.prev = node
        self.size += 1

    def remove_node(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        node.prev = None
        node.next = None
        self.size -= 1

    def remove_head(self):
        if self.size > 0:
            node = self.head.next
            self.remove_node(node)
            return node
        else:
            return None

    def get_size(self):
        return self.size


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # if capacity <= 0:
        #     raise ValueError("Capacity can not be zero")
        self.capacity = capacity
        self.key_to_node = {}  # {key: ListNode}
        self.freq_to_lru = collections.defaultdict(LRU)  # {freq: LRU}
        self.min_freq = 0  # we need to maintain it for eviction

    def increase_freq(self, node):
        # increase the frequency of node by one,
        # and move the node from current lru to a higher freq lru
        old_freq = node.freq
        new_freq = old_freq + 1
        node.freq += 1
        old_lru = self.freq_to_lru[old_freq]
        old_lru.remove_node(node)
        new_lru = self.freq_to_lru[new_freq]
        new_lru.add_node_to_tail(node)
        if old_lru.get_size() == 0 and old_freq == self.min_freq:
            self.min_freq += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node or self.capacity == 0:
            return -1
        node = self.key_to_node[key]
        self.increase_freq(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.increase_freq(node)
        else:
            if len(self.key_to_node) == self.capacity:
                node = self.freq_to_lru[self.min_freq].remove_head()
                # we don't have to update self.min_freq here, because it will be 1
                del self.key_to_node[node.key]
            node = ListNode(key, value)
            self.min_freq = 1
            self.key_to_node[key] = node
            lru = self.freq_to_lru[1]
            lru.add_node_to_tail(node)


"""
Design and implement a data structure for Least Frequently Used (LFU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, 
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions 
for that item since it was inserted. This number is set to zero when the item is removed.


Follow up:
Could you do both operations in O(1) time complexity?


Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

