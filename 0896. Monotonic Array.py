# method 2
# time O(n), space O(1)
# use two flags, code is cleaner than method 1


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = False
        decreasing = False
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                increasing = True
            elif A[i] > A[i+1]:
                decreasing = True
            if increasing and decreasing:
                return False
        return True


# method 1
# use a single flag


class Solution1(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # edge case
        if not A or len(A) < 3:
            return True
        # find first different item
        for i in range(len(A)-1):
            if A[i] != A[i+1]:
                break
        if A[i] > A[i+1]:
            increasing = -1
        else:
            increasing = 1
        # check the rest items
        for j in range(i+1, len(A)-1):
            if (A[j+1]-A[j])*increasing < 0:
                return False
        return True


"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  
An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.


Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""
