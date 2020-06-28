# time O(n*log(n)), space O(n)
# greedy, meet small elements in B first, and use as small element in A as possible


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        pairs_B = [(b, i) for i, b in enumerate(B)]
        pairs_B.sort()
        A.sort()
        not_used = []
        res = []
        iA = 0
        for b, i in pairs_B:
            while iA < len(A) and A[iA] <= b:
                not_used.append(A[iA])
                iA += 1
            if iA < len(A):
                res.append((i, A[iA]))
                iA += 1  # do not forget
            else:
                res.append((i, not_used.pop()))
        res.sort()
        return [num for i, num in res]


"""
Given two arrays A and B of equal size, the advantage of A with respect to B 
is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
