# method 2, generate all possible double-digit numbers
# code is much cleaner


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        digits = sorted(set(hour+minute))
        numbers = [x + y for x in digits for y in digits]  # generate all candidates

        i = numbers.index(minute)  # note that hour and minute must exists in numbers
        if i + 1 < len(numbers) and numbers[i+1] < '60':
            return hour + ":" + numbers[i+1]

        i = numbers.index(hour)
        if i + 1 < len(numbers) and numbers[i+1] < '24':
            return numbers[i+1] + ":" + numbers[0]

        return numbers[0] + ":" + numbers[0]





# method 1, check digit by digit, 5 checks in total, very verbose

import bisect


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        digits = sorted(set(hour + minute))
        # last digit for minute
        i = bisect.bisect_right(digits, minute[-1])
        if i < len(digits):
            return hour + ":" + minute[:-1] + digits[i]
        # second last for minute
        if len(minute) == 1:
            i = bisect.bisect_right(digits, '0')
        else:
            i = bisect.bisect_right(digits, minute[0])
        if i < len(digits) and digits[i] < '6':
            return hour + ":" + digits[i] + digits[0]  # reset last num to digits[0]

        # last digit for hour
        i = bisect.bisect_right(digits, hour[-1])
        if i < len(digits) and int(hour[:-1] + digits[i]) < 24:
            return hour[:-1] + digits[i] + ":" + digits[0] * 2
        # second last for hour
        if len(hour) == 1:
            i = bisect.bisect_right(digits, '0')
        else:
            i = bisect.bisect_right(digits, hour[0])
        if i < len(digits) and digits[i] < '3':
            return digits[i] + digits[0] + ":" + digits[0] * 2

        return digits[0] * 2 + ":" + digits[0] * 2


"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" 
are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  
It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed 
that the returned time is next day's time since it is smaller than the input time numerically.
"""

