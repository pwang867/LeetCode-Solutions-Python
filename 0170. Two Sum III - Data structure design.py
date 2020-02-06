# method 3, use set to save all sums, and use set to save all numbers, add O(n), find O(1), space O(n^2)

# method 2, use Counter dict {num: counts}, add O(1), find O(n), space O(n)

# method 1, use array, add O(n), find O(n), space O(n)
import bisect
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        bisect.insort(self.arr, number)
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        left, right = 0, len(self.arr)-1
        while left < right:
            total = self.arr[left] + self.arr[right]
            if total == value:
                return True
            elif total > value:
                right -= 1
            else:
                left += 1
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

