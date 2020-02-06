# note: whenever arr is sorted, consider about binary search


# binary search, O(log(n))
class Solution1(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        delta = (arr[-1] - arr[0])//len(arr)
        left, right = 0, len(arr)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if arr[mid]-arr[left] == delta*(mid-left):
                left = mid
            else:
                right = mid
        return (arr[left] + arr[right])//2

# method 2: O(n), use math
class Solution(object):
    def missingNumber(self, arr):
        return (arr[0] + arr[-1])*(len(arr) + 1)//2 - sum(arr)


# method 3: O(n)
class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr or len(arr) < 2:
            return None
        if len(arr) == 2:
            return (arr[0] + arr[1])//2
        
        for i in range(len(arr)-2):
            gap1 = arr[i+1] - arr[i]
            gap2 = arr[i+2] - arr[i+1]
            if gap1 == gap2*2:
                return (arr[i+1] + arr[i])//2
            elif gap1*2 == gap2:
                return (arr[i+2] + arr[i+1])//2
        
        return None



"""
In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array.

Return the removed value.

 

Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].
 

Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5  
"""

arr = [15,13,12]
print(Solution().missingNumber(arr))
