"""
Find the length of the longest sub string without repeating charecters of a given string?

string: 'abceadg'
return: 'bceadg', 4

method 1:
brute force, two for loops, O(n^2), space O(res)

'abceadg'
 i
     j
 hashset
 res = max(res, j-i)


method 2:
sliding window approach, O(n), O(n)
'abceadg'
  i
     j
 hashset
 res = max(res, j-i+1)

'aaaaaa'

'abcdfs'

"""


class Solution:
    def longest_substring_without_duplicates(self, s):  # s='abceadg'
        if s:
            return 0
        window = set()  # windo = set()
        left = 0
        max_len = 0
        for right in range(len(s)):  # right = 6
            # check s[right] is in hashset, and adjust left pointer if it in
            if s[right] in window:  # 'a', window = {'a', 'b', 'c', 'e'}
                while left <= right and s[left] != s[right]:  # left=0
                    left += 1
                    window.remove(s[left])
                left += 1  # left = 1
            else:
                # add s[right] to hashset
                window.add(s[right])  # window = {'a', 'b', 'c', 'e', 'd', 'g'}
            # update max_len
            max_len = max(max_len, right - left + 1)  # max_len = 6
        return max_len  # 6


"""
method
2:
sliding
window
approach, O(n), O(n)
'abceadg'
i
j
hashset
res = max(res, j - i + 1)
"""
