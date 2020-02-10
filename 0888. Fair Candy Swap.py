# hashset, time/space O(n)
# solution 3: O(min(m,n)), using set
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if len(A) < len(B):
            A, B = B, A
            swapped = True
        else:
            swapped = False
        
        target = (sum(A) - sum(B))/2
        B_set = set(B)
        ans = []
        for candy in A:
            if candy - target in B_set:
                ans = [candy, candy-target]
                break
        
        if swapped:
            ans.reverse()
        
        return ans
        

# https://leetcode.com/problems/fair-candy-swap/
# follow-up: how about multiple swaps are allowed?
class Solution1:
    def fairCandySwap(self, A, B):
        used = [0 for i in range(len(B))]
        diff = sum(A) - sum(B)
        if diff%2 != 0:
            return []
        ans = []
        path = []
        self.swapHelper(A, 0, B, 0, used, diff, path, ans)
        return ans
        
    
    def swapHelper(self, A, i, B, k, used, diff, path, ans):
        # only swap candy between A[i:] and B[k:]
        # i is current index of A
        if k > len(B) - 1:
            return
        if i > len(A) - 1:
            return
        
        # no swap for index i
        self.swapHelper(A, i+1, B, k, used, diff, path, ans)
        
        for j in range(k, len(B)):
            
            if used[j] == 1:  # B[j] has been swapped
                continue
            # try to swap A[i] with B[j] one by one
            path.append((A[i], B[j]))
            used[j] = 1
            diff = diff - 2*(A[i]-B[j])
            if diff == 0:
                ans.append(path + [])
                self.swapHelper(A, i+1, B, j+1, used, 0, [], ans)
            else:
                self.swapHelper(A, i+1, B, j+1, used, diff, path, ans)  # avoid duplicates such as [(1,5), (5,2)] and [(1,2), (5,5)]
            path.pop()
            used[j] = 0
            diff = diff + 2*(A[i]-B[j])


"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the 
i-th bar of candy that Alice has, and B[j] is the size of the 
j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that 
after the exchange, they both have the same total amount of candy.  
(The total amount of candy a person has is the sum of the sizes of 
candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy 
bar that Alice must exchange, and ans[1] is the size of the candy bar 
that Bob must exchange.

If there are multiple answers, you may return any one of them.  
It is guaranteed an answer exists.

 

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]
 

Note:

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
It is guaranteed that Alice and Bob have different total amounts of candy.
It is guaranteed there exists an answer.
"""


            
if __name__ == "__main__":
    print(Solution().fairCandySwap([8,73,2,86,32], [56,5,67,100,31]))
