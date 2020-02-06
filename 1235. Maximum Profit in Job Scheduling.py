# sort by EndTime, and then dp
# time O(n*log(n)), space O(n)
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        if not startTime:
            return 0
        arr = []
        n = len(startTime)
        for i in range(n):
            arr.append((endTime[i], startTime[i], profit[i]))
        arr.sort()  # sort in endtime
        
        dp = [0]*n
        dp[0] = arr[0][2]
        for i in range(1, n):
            dp[i] = dp[i-1]  # not selecting arr[i]
            j = self.search(arr, 0, i-1, arr[i][1])  # select arr[i]
            pre = dp[j] if j != -1 else 0
            dp[i] = max(dp[i], pre + arr[i][2])
        
        return dp[-1]
    
    def search(self, arr, left, right, maxEnd):
        # find the last arr whose endTime doesn't intersect with maxEnd
        while left + 1 < right:
            mid = left + (right-left)//2
            if arr[mid][0] <= maxEnd:
                left = mid
            else:
                right = mid
        if arr[right][0] <= maxEnd:
            return right
        elif arr[left][0] <= maxEnd:
            return left
        else:
            return -1

startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
print(Solution().jobScheduling(startTime, endTime, profit))


"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:




Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
