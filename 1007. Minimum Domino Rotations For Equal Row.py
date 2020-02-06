# time O(n), space O(1)
# we need to switch A[i] and B[i] until A or B is filled with only one common number
# the common number must be either A[0] or B[0], or other pairs (A[1], B[1])
# for each candidate, we need to consider 
# if we need to make candidates in A or make candidates in B
# so in total we have four conditions
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A:
            return 0
        
        # check if the common number could be A[0]
        num_rotation = self.getNumOfRotation(A, B, A[0])
        if num_rotation != -1:  # -1 means rotation is not possible
            return num_rotation  # don't have to check B[0] any more if A[0] is OK because the result will be the same
        
        # check if the common number could be B[0]
        return self.getNumOfRotation(A, B, B[0])
    
    def getNumOfRotation(self, A, B, candidate):
        cntA, cntB = 0, 0
        for i in range(len(A)):  # corner case: A[i] == B[i] == candidate
            if A[i] == candidate:
                cntA += 1
            if B[i] == candidate:
                cntB += 1
            if A[i] != candidate and B[i] != candidate:
                return -1
        # the candidate may be aligned in the upper or lower row
        return min(len(A)-cntA, len(A)-cntB)  



"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves 
of the i-th domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

"""
