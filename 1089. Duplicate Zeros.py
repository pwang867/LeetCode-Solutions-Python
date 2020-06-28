# inplace, time O(n), space O(1)


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if not arr or len(arr) < 2:
            return
        n = len(arr)
        total = 0
        end = 0
        for i, num in enumerate(arr):
            if num == 0:
                total += 2
            else:
                total += 1
            if total >= n:  # might overshoot at most one
                end = i
                break

        # two pointers
        if total == n:
            j = n - 1
        elif total == n + 1:  # overshoot
            end -= 1
            arr[n - 1] = 0
            j = n - 2
        while end >= 0:
            if arr[end] != 0:
                arr[j] = arr[end]
                j -= 1
            else:
                arr[j] = 0
                arr[j - 1] = 0
                j -= 2
            end -= 1


"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.


Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""