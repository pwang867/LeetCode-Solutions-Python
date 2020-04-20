# O(n*log(n)), rolling hash + binary search


class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        left, right = 1, len(S) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.has_dup_with_length(S, mid) != -1:
                left = mid
            else:
                right = mid
        i = self.has_dup_with_length(S, right)
        if i != -1:
            return S[i - right + 1:i + 1]
        else:
            i = self.has_dup_with_length(S, left)
            return S[i - left + 1:i + 1]

    def has_dup_with_length(self, S, length):
        # return -1 if not exists, otherwise return the end index
        visited = collections.defaultdict(list)  # {val: a list of start index to resolve hash conflict}
        hash_val = 0
        base = 26
        N = 10 ** 9 + 7
        factor = (base ** (length - 1)) % N
        for i in range(length):
            hash_val = (hash_val * base + ord(S[i]) - ord('a')) % N
        visited[hash_val].append(length - 1)
        for i in range(length, len(S)):
            hash_val -= (ord(S[i - length]) - ord('a')) * factor
            hash_val = hash_val * base + (ord(S[i]) - ord('a'))
            hash_val %= N
            if hash_val in visited:
                for j in visited[hash_val]:
                    if self.match(S, i, j, length):
                        return i
            visited[hash_val].append(i)
        return -1

    def match(self, S, i, j, length):
        for k in range(length):
            if S[i - k] != S[j - k]:
                return False
        return True


"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)



Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""


Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""