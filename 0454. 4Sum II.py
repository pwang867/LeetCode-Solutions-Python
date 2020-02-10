# Do it two by two to save memory
# Using dict to save cnts
# O(N^2)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        for a in A:
            for b in B:
                key = a + b
                dic[key] = dic.get(key, 0) + 1
        res = 0
        for c in C:
            for d in D:
                res += dic.get(-c-d, 0)
        return res
    

        
# method 1, Brute force, time limit exceeded
class Solution1(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans = []
        if len(A)*len(B)*len(C)*len(D) == 0:
            return 0
       
        for i in range(len(A)):
            for j in range(len(B)):
                temp = A[i] + B[j]
                for k in range(len(C)):
                    temp += C[k]
                    for l in range(len(D)):
                        if temp + D[l] == 0:
                            ans.append([i, j, k, l])
                    temp -= C[k]
        return len(ans)
    


"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
