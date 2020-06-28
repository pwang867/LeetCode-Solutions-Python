# use max_cnt buckets, and do round robbin when assign tasks into the buckets
# the bucket min size will be n+1
# divide the buckets into 3 regions: region M, region N, and last single bucket

import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0
        cnts = collections.Counter(tasks)
        max_cnt = max(cnts.values())

        # the implementation below is for faster speed, but can be simpler
        if max_cnt == 1:
            return len(tasks)
        num_max_cnt = 0
        sum_non_max_cnts = 0
        for task, cnt in cnts.items():
            if cnt == max_cnt:
                num_max_cnt += 1
            else:
                sum_non_max_cnts += cnt
        M = sum_non_max_cnts % (max_cnt-1)
        N = max_cnt - 1 - M
        sizeN = num_max_cnt + (sum_non_max_cnts)//(max_cnt-1)
        sizeM = sizeN + 1
        return max(sizeM, n+1)*M + max(sizeN, n+1)*N + num_max_cnt*1   # mistake: n+1


"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z 
where different letters represent different tasks. Tasks could be done without original order. 
Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.


Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
