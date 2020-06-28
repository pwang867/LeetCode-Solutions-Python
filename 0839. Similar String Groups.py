# method 1, union find, O(m*m*n), m = len(A), n = len(A[i])


class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = list(set(A))
        parent = {i: i for i in range(len(A))}
        size = {i: 1 for i in range(len(A))}

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

        def similar(u, v):
            if len(u) != len(v):
                return False
            cnt = 0
            for i in range(len(u)):
                if u[i] != v[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 0 or cnt == 2

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if similar(A[i], A[j]):
                    union(i, j)

        map(find, parent)
        return len(set(parent.values()))


"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?



Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2


Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
"""