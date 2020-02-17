"""
from: Google

You are given a list of jobs, each with a deadline, 
and requires a certain amount of time to be completed.

Each worker can perform 1 job at a time. 
What is the minimum number of workers required to be able to complete all jobs 
within the deadline?

Deadlines are listed in terms of days after the start. A job with deadline of 1 
and duration of 1 means that this job is due on Day 1 and 
requires 1 day to complete.

Example:

deadlines = [3, 2, 3]
durations = [2, 1, 1]
Answer: 2
Explanation: Use 1 worker for jobs 1 and 2, Use another worker for job 3.
"""

# ref: https://leetcode.com/playground/5FDM4Ltv
# using heap, time O(n*log(n)), space O(n)
# greedy, might be wrong
import heapq
class Solution:
    
    def minWorker(self, deadlines, durations):
        if not deadlines: return 0
        tasks = [(deadlines[i], durations[i]) for i in range(len(deadlines))]       
        tasks.sort()
        workers = [0]   # saves the finishing time of each worker
        for task in tasks:
            deadline, duration = task
            if workers[0] + duration <= deadline:
                time = heapq.heappop(workers)
                heapq.heappush(workers, time + duration)
            else:   # start a new worker
                heapq.heappush(workers, duration)
        return len(workers)

deadlines = [3, 2, 3]
durations = [2, 1, 1]
print(Solution().minWorker(deadlines, durations))

