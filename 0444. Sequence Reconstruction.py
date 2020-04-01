# edge case 1: [1], [[1],[2,3],[3,2]]
# edge case 2: [1], [[1], [1], [1]]

from collections import defaultdict, deque
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(set)
        for seq in seqs:
            if len(seq) == 1:        # seq might be one element
                if seq[0] not in graph:
                    graph[seq[0]] = set()
            for i in range(1, len(seq)):
                u, v = seq[i-1], seq[i]
                graph[u].add(v)
        indegrees = defaultdict(int)
        for u, children in graph.items():
            if u not in indegrees:    # don'g forget some nodes
                indegrees[u] = 0
            for v in children:
                indegrees[v] += 1
        queue = deque(key for key, val in indegrees.items() if val == 0)
        res = []
        while queue:
            if len(queue) > 1:
                return False
            u = queue.popleft()
            res.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)
        # easy to miss: len(res) == len(indegrees)
        return len(res) == len(indegrees) and res == org   


"""
Check whether the original sequence org can be uniquely reconstructed 
from the sequences in seqs. The org sequence is a permutation of the integers 
from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest 
common supersequence of the sequences in seqs (i.e., a shortest sequence so 
that all sequences in seqs are subsequences of it). Determine whether there 
is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, 
because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the 
original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
UPDATE (2017/1/8):
The seqs parameter had been changed to a list of list of strings 
(instead of a 2d array of strings). Please reload the code definition to 
get the latest changes.
"""
