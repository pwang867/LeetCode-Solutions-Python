# method 2: use buckets to sort faster, time O(n), space O(n)
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for letter in s:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        
        buckets = [[] for i in range(len(s)+1)]
        for letter, cnt in d.items():
            buckets[cnt].append(letter)
        
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for letter in buckets[i]:
                res.append(letter*i)
        return "".join(res)


# method 1: use Counter, time: O(n+n*log(n))
import collections
class Solution1(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.Counter(s)
        pairs = d.most_common()  # a list of (key, cnt) pairs sorted by cnt
        res = []
        for letter, freq in pairs:
            res.append(letter*freq)
        return "".join(res)
    


"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
