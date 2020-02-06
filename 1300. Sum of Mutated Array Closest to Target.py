# method 2, binary search, time O(n*log(max(arr))), space O(1)
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if not arr:
            return None
        right = max(arr)
        if target >= right*len(arr):
            return right
        left = target//len(arr) - 1
        res = right
        min_diff = abs(sum(arr) - target)
        while left + 1 < right:
            mid = left + (right-left)//2
            diff = self.getValue(arr, mid) - target
            if diff == 0:
                return mid
            elif diff > 0:
                right = mid
            else:
                left = mid
            if abs(diff) < min_diff or (abs(diff) == min_diff and mid < res):
                res = mid
                min_diff = abs(diff)
        return res
        
    def getValue(self, arr, value):
        res = 0
        for num in arr:
            if num <= value:
                res += num
            else:
                res += value
        return res
    

# method 1, sort, time O(nlog(n))
class Solution1(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort(reverse=True)
        ans = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        if not arr:
            return ans
        a = target/len(arr)
        a = a if abs(a*len(arr)-target) <= abs((a+1)*len(arr)-target) else a+1
        return a


"""
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5
"""
