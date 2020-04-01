# method 2, backward dynamical programing, time O(n*B), space O(n)
# to reduce space, we need another array next[], where next[i] means the next position after i
# we can travel backwards to calculate cost[n-1] to cost[0]
# cost[i] means the cost starting from i to n-1
# we can use cost[j] to update cost[i], j needs to go from i+1 to i+B








# if arr1 < arr2, then this might not be true: arr1 + [n] < arr2 + [n]
# for example, [1] < [1, 2], but [1, 3] > [1, 2, 3]

# edge case: [0,0,0,0,0,0], 3

# time O(n*B), space O(n^2)
# dynamical programming, paths[i] is the cheapest / lexicographically smallest
# path to go from 0 to i
class Solution1(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A: return []
        if len(A) == 1: return [1]
        n = len(A)
        cost = [float('inf')]*n
        cost[0] = A[0]       # don't forget
        paths = [[]]*n
        paths[0] = [1]
        for i in range(1, n):
            a = A[i]
            if a == -1:
                continue
            for j in range(i-1, i-B-1, -1):
                if j < 0:
                    break
                if A[j] == -1:
                    continue
                if cost[j] < cost[i] or \
                (cost[j] == cost[i] and paths[j] + [i+1] < paths[i]):
                    cost[i] = cost[j]
                    paths[i] = paths[j] + [i+1]
            if paths[i] == []:   # if we cannot arrive at i, then we can not arrive any position after i
                return []
            cost[i] += a
        return paths[-1]



"""
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:

Input: [1,2,4,-1,2], 2
Output: [1,3,5]
 

Example 2:

Input: [1,2,4,-1,2], 1
Output: []
 

Note:

Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
Length of A is in the range of [1, 1000].
B is in the range of [1, 100].
"""
