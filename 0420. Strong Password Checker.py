# time can be optimized to O(n), space O(n)


import collections


class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        LEN_LOWER_LIMIT = 6
        LEN_UPPER_LIMIT = 20
        length = len(s)
        has_lower, has_upper, has_digit = False, False, False
        repeats = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True
            start = i
            while i < len(s) and s[i] == s[start]:
                i += 1
            if i - start >= 3:  # don't forget this condition
                repeats.append(i - start)
        cnt_missing_type = 3 - (int(has_lower) + int(has_upper) + int(has_digit))

        # remove all duplicates
        repeats.sort(key=lambda x: x % 3)  # edge case: "AAAAAABBBBBB123456789a", can be optimized by bucket sort
        repeats = collections.deque(repeats)
        num_changes = 0
        while repeats:
            x = repeats.popleft()
            if length < LEN_LOWER_LIMIT:
                # insert
                new_insert = x // 3
                num_changes += new_insert
                length += new_insert
                cnt_missing_type -= new_insert
            elif length > LEN_UPPER_LIMIT:
                # delete
                if x % 3 == 0:
                    new_del = 1
                elif x % 3 == 1:
                    new_del = min(2, length - LEN_UPPER_LIMIT)
                else:
                    new_del = min(x - 2, length - LEN_UPPER_LIMIT)
                num_changes += new_del
                length -= new_del
                x -= new_del
                if x > 2:
                    repeats.append(x)
            else:
                # replace
                new_replace = x // 3
                num_changes += new_replace
                cnt_missing_type -= new_replace

        # deal with missing types
        cnt_missing_type = max(cnt_missing_type, 0)
        if length < LEN_LOWER_LIMIT:
            # insert
            length += cnt_missing_type
            num_changes += cnt_missing_type
        else:
            # replace
            num_changes += cnt_missing_type

        # deal with length
        if length < LEN_LOWER_LIMIT:
            # insert
            num_changes += LEN_LOWER_LIMIT - length
        elif length > LEN_UPPER_LIMIT:
            # delete
            num_changes += length - LEN_UPPER_LIMIT

        return num_changes


"""
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, 
but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, 
and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.

Accepted
"""
