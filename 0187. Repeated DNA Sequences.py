# method 2, bit manipulation, time/space O(res), no waste of space
"""
0 = 00 (bits in binary number system) = 'A'
1 = 01 (bits in binary number system) = 'C'
2 = 10 (bits in binary number system) = 'G'
3 = 11 (bits in binary number system) = 'T'

A A C C T C C G G T

00 00 01 01 11 01 01 10 10 11 = 00000101110101101011 (binary) = 23915 (decimal)
"""
from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {"A": 0, "C": 1, "G": 2, "T": 3}   # encoding map
        mask = (1<<20) - 1     # mistake: (2<<20) - 1
        seen = defaultdict(int)
        res = []
        cur = 0    # the encoded string as a 20-bit integer (use 4-byte)
        for i in range(len(s)):
            cur = cur << 2
            cur |= d[s[i]]
            if i < 9:
                continue
            cur &= mask     # only keep the last 20-bit
            seen[cur] += 1      
            if seen[cur] == 2:   # be careful here for those three sentences
                res.append(s[i-9:i+1])
        return res



# method 1, brute force, time/space O(10*n)
# a lot of wasting space
from collections import defaultdict
class Solution1(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N = 10
        if not s or len(s) < N:
            return []
        
        d = defaultdict(int)  # {subsequence: counts}
        for i in range(len(s)-N+1):
            d[s[i:i+N]] += 1
        
        res = []
        for key, value in d.items():
            if value > 1:
                res.append(key)
        return res



"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

