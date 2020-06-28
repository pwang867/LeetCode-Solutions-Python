# time O(len(A)*sqrt(A[i])), space O(primes)


class UnionFind:
    def __init__(self, nodes):
        self.parents = {node: node for node in nodes}
        self.sizes = {node: 0 for node in nodes}

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        parentu, parentv = self.find(u), self.find(v)
        if parentu != parentv:
            if self.sizes[parentu] < self.sizes[parentv]:
                parentu, parentv = parentv, parentu
            self.parents[parentv] = parentu
            self.sizes[parentu] += self.sizes[parentv]
            return True
        return False

    def increase_size(self, u):
        p = self.find(u)
        self.sizes[p] += 1

    def get_largest_component_size(self):
        if not self.sizes:
            return 0
        return max(self.sizes.values())


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        if A == [1]: return 1
        primes = self.get_all_primes(max(A))
        primes_set = set(primes)
        uf = UnionFind(primes)
        for a in A:
            pre_prime = -1
            for prime in primes:  # for loop will terminate when prime > sqrt(a)
                if a in primes_set:  # optimize for prime numbers
                    if pre_prime == -1:
                        uf.increase_size(a)
                    else:
                        uf.union(pre_prime, a)
                    break
                if a % prime != 0: continue
                while a % prime == 0:  # optimization
                    a //= prime
                if pre_prime == -1:
                    uf.increase_size(prime)
                else:
                    uf.union(pre_prime, prime)
                pre_prime = prime

        return uf.get_largest_component_size()

    def get_all_primes(self, n):
        primes = []
        is_prime = [True] * (n + 1)
        for num in range(2, n + 1):
            if is_prime[num]:
                primes.append(num)
                x = num * 2
                while x <= n:
                    is_prime[x] = False
                    x += num
        return primes


"""
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""
