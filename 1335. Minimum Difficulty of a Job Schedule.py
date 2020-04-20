# dp[i][j] means the minimum total difficulty to divide jobDifficulty[:j+1] into i groups
# time O(d*n*n), space O(d*n)

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if not jobDifficulty or d > len(jobDifficulty):
            return -1
        n = len(jobDifficulty)
        dp = [[float('inf')]*n for _ in range(d+1)]
        cur = 0
        for i in range(n):   # initialization
            cur = max(cur, jobDifficulty[i])
            dp[1][i] = cur
        for day in range(2, d+1):
            for i in range(day-1, n):
                last = 0
                for j in range(i, day-2, -1):
                    last = max(last, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], last + dp[day-1][j-1])
        return dp[d][n-1]
    


# time O(d*n*n), space O(d*n)
class Solution2(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if d > len(jobDifficulty):
            return -1
        self.memo = {}
        return self.dfs(jobDifficulty, 0, d)
    
    def dfs(self, jobs, i, days):
        if (i, days) in self.memo:
            return self.memo[(i, days)]
        if days == 1:
            self.memo[(i, days)] = max(jobs[i:])
            return self.memo[(i, days)]
        cur = 0
        res = float('inf')
        for j in range(i, len(jobs)-days+1):
            cur = max(cur, jobs[j])
            res = min(res, cur + self.dfs(jobs, j+1, days-1))
        self.memo[(i, days)] = res
        return res
    

# dp, time/space O(d*n*n)
class Solution1(object):
    
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if d > len(jobDifficulty): return -1
        self.memo = {}
        return self.dfs(jobDifficulty, 1, d-1, jobDifficulty[0], jobDifficulty[0])
    
    def dfs(self, jobs, i, days, cur_diff, total_diff):
        # return the total difficulty when we already processed jobs[:i] 
        # and have days left, and the current day's difficulty is cur_diff
        if len(jobs) - i < days:
            return -1
        if (i, days, cur_diff) in self.memo:
            return total_diff + self.memo[(i, days, cur_diff)]
        if i == len(jobs):
            return total_diff if days == 0 else -1
        res = float('inf')
        if days - 1 >= 0 and len(jobs) - i - 1 >= days - 1:  # use a new day
            res = min(res, self.dfs(jobs, i+1, days-1, jobs[i], total_diff+jobs[i]))
        if days >= 0 and len(jobs) - i - 1 >= days:   # use existing
            new_cur = max(cur_diff, jobs[i])
            res = min(res, self.dfs(jobs, i+1, days, new_cur, total_diff+new_cur-cur_diff))
        self.memo[(i, days, cur_diff)] = res - total_diff
        return res
        
        
        
"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 

Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843
"""
