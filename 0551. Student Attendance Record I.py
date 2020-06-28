# line sweep, time O(n), space O(1)


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n_A, n_L = 0, 0
        for c in s:
            if c == "P":
                n_L = 0
            elif c == "A":
                n_L = 0     # clear n_L, easy to miss
                n_A += 1
                if n_A > 1:
                    return False
            elif c == "L":
                n_L += 1
                if n_L > 2:
                    return False
        return True


"""
You are given a string representing an attendance record for a student. 
The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) 
or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""
