# method 2: union find

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        if not row:
            return 0
        N = len(row)//2
        parent = {i:i for i in range(2*N)}
        size = {i:1 for i in range(2*N)}
        
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            return False
        
        for i in range(0, 2*N, 2):
            union(i, i+1)   # union couples
            union(row[i], row[i+1])  # union neighbors
        map(find, parent)
        roots = set(parent.values())
        swap = 0
        for root in roots:
            swap += size[root]//2 - 1
        return swap
    

# method 1
# the seats of the couple don't matter, 
# as long as the couple is sitting together
# paired seats can be saved into a dictionary

class Solution1(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        d = {}
        for i in range(0, len(row), 2):
            d[row[i]] = row[i+1]
            d[row[i+1]] = row[i]
        
        cnt = 0
        s = set(d.keys())
        while s:
            x1 = s.pop()
            y1 = d[x1]
            if y1 != x1^1:
                # when a swap is needed
                # {x1:y1, x2:y2} becomes {x1:x2, y1:y2}
                cnt += 1
                x2 = x1^1
                y2 = d[x2]
                d[y1] = y2
                d[y2] = y1
                s.remove(x2)
            else:
                s.remove(y1)
        
        return cnt
    

    
"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""

