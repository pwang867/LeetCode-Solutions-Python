# time O(n), space O(res)

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        res = []
        i, j, k = 0, 0, 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            elif arr2[j] > arr3[k]:
                k += 1
            elif arr2[j] < arr3[k]:
                i += 1
                j += 1
            else:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
        return res


"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.


Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
 

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""
