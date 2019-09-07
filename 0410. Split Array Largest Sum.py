# method 3: tricky method, binary search of the result
# time O(n*log(sum(nums) - max(nums))), space O(n)
class Solution(object):
    def splitArray(self, nums, m):
        # the boundary of the result
        high = sum(nums)
        low = max(nums)
        if m == 1:
            return high
        if m >= len(nums):
            return low
        
        while low <= high:
            mid = low + (high - low)//2
            cnt = self.countGroups(nums, mid)
            if cnt <= m:
                high = mid - 1
            else:
                low = mid + 1
        
        return low
    
    def countGroups(self, nums, maxSum):
        # split nums into groups with sum no larger to maxSum
        # return the number of groups
        cnt = 0
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total > maxSum:
                cnt += 1
                total = num
        
        return cnt + 1  # mistake: return cnt


# method 2: based on method 1, but use binary search to search k
# time O(m*n*log(n)), space O(m*n)
class Solution2(object):
    def splitArray(self, nums, m):
        n = len(nums)
        sums = [0]*n
        total = 0
        for i, num in enumerate(nums):
            total += num
            sums[i] = total
        
        dp = [[float('inf')]*n for _ in range(m+1)]
        dp[1] = sums + []
        for i in range(2, m+1):
            for j in range(i-1, n):  # don't have to start with 0
                
                # binary search, because temp will be monotonous
                left, right = i-2, j
                while left + 1 < right:
                    mid = (left + right)/2
                    temp = dp[i-1][mid] - (sums[j] - sums[mid])
                    if temp == 0:
                        dp[i][j] = dp[i-1][mid]
                        break
                    elif temp > 0:
                        right = mid
                    else:
                        left = mid
                
                dp[i][j] = min(dp[i][j], 
                               max(dp[i-1][left], sums[j]-sums[left]),
                               max(dp[i-1][right], sums[j]-sums[right]))
        
        return dp[m][n-1]
    


# method 1: dp, time O(m*n^2), space O(m*n)
# dp[i][j] means partition nums[:j+1] into i groups
# dp[i][j] = max(dp[i-1][k], sums[j]-sums[k]) for 1 <= k <= j
class Solution1(object):
    def splitArray(self, nums, m):
        n = len(nums)
        sums = [0]*n
        total = 0
        for i, num in enumerate(nums):
            total += num
            sums[i] = total
        
        dp = [[0]*n for _ in range(m+1)]
        dp[1] = sums + []
        for i in range(2, m+1):
            for j in range(n):
                dp[i][j] = float('inf')
                for k in range(j+1):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k], sums[j]-sums[k]))
        
        return dp[m][n-1]
        


# method 0: wrong solution
# greedy, calculate the sums array first, 
# and then each time get a partition closest to average of the rest of array
# fails in this case: nums = [1, 4, 4], m = 3
import bisect
class Solution0(object):  # wrong solution
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        sums = [0]*len(nums)
        total = 0
        for i, num in enumerate(nums):
            total += num
            sums[i] = total
        
        start = 0  # the start index of the next partition
        partition = []
        min_res = min(nums)
        res = min_res  # max sum
        while start < len(nums):
            average = (sums[-1] - sums[start] + nums[start])*1.0/m
            average = max(average, min_res)
            target = sums[start] - nums[start] + average
            if m == 1:
                res = max(res, sums[-1] - sums[start] + nums[start])
                break
            # greedy, find the sums[i] closest to target
            i = bisect.bisect_left(sums, target)
            # print(i, target, sums)
            if i > 0 and abs(target - sums[i-1]) < abs(sums[i] - target):
                # i is the end index of this partition
                i -= 1
            if start == 0:
                res = sums[i]
            else:
                res = max(res, sums[i] - sums[start-1])
            partition.append(i)
            start = i + 1
            m -= 1
            # print(start, m)
        
        # print(partition)
        return res
    
