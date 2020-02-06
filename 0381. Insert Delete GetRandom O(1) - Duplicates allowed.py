from collections import defaultdict
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(set)
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = True
        if val in self.d:
            res = False
        self.nums.append(val)
        self.d[val].add(len(self.nums)-1)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False

        if val == self.nums[-1]:
            self.d[val].remove(len(self.nums)-1)
        else:
            i = self.d[val].pop()
            self.nums[i] = self.nums[-1]
            self.d[self.nums[i]].remove(len(self.nums)-1)
            self.d[self.nums[i]].add(i)

        if not self.d[val]:
            del self.d[val]
        self.nums.pop()
        return True


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""
