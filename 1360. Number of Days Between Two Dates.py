import datetime


class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        dt1 = self.get_datetime(date1)
        dt2 = self.get_datetime(date2)
        return abs((dt1 - dt2).days)
    
    def get_datetime(self, datestr):
        arr = map(int, datestr.split('-'))
        return datetime.datetime(arr[0], arr[1], arr[2])


"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""
