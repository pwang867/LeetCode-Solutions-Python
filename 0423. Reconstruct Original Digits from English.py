# method 2, better than method 1
# https://leetcode.com/problems/reconstruct-original-digits-from-english
# /discuss/91207/one-pass-O(n)-JAVA-Solution-Simple-and-Clear




# method 1, each digit has a unique letter


"""
'z', '0', 'zero'
'w' '2' 'two'
'x', '6', 'six'
'u', '4', 'four'
'g', '8', 'eight'

't', '3', 'three'
'f', '5', 'five'
's', '7', 'seven'
'o', '1', 'one'

'e', '9', 'nine'

"""


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        seq = [('z', '0', 'zero'), ('w', '2', 'two'), ('x', '6', 'six'),
               ('u', '4', 'four'), ('g', '8', 'eight'), ('t', '3', 'three'),
               ('f', '5', 'five'), ('s', '7', 'seven'), ('o', '1', 'one'),
               ('e', '9', 'nine')]
        digit_counts = {str(i): 0 for i in range(10)}
        s_counter = collections.Counter(s)
        for c, digit, english in seq:
            if s_counter.get(c, 0) > 0:
                cnt = s_counter[c]
                digit_counts[digit] = cnt
                for c_del in english:    # remove all letters that are used
                    s_counter[c_del] -= cnt
        res = []
        for digit in range(10):
            digit = str(digit)
            res.append(digit * digit_counts[digit])
        return "".join(res)


"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, 
output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. 
That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""