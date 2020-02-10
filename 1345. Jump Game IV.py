# BFS, O(n), need to delete the d[arr[i]]
from collections import deque, defaultdict
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr or len(arr) == 1:
            return 0
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
        n = len(arr)
        visited = [False]*n
        visited[0] = True
        queue = deque([0])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == n-1:
                    return depth
                for p in d[arr[i]] + [i+1, i-1]:
                    if 0 <= p < n and not visited[p]:
                        visited[p] = True
                        queue.append(p)
                del d[arr[i]]   # important, must have this line, otherwise, time complexity is O(n^2)
            depth += 1
        


"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
"""
