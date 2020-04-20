# sliding window
class Solution(object):
    def countAndSay(self, n, pre="1"):
        """
        :type n: int
        :rtype: str
        """
        if n < 0:
            return ""

        for _ in range(n-1):
            # use pre to generate cur
            count = 1
            cur = []
            for i in range(1, len(pre)):
                # search count of repeating number
                if pre[i] == pre[i-1]:
                    count += 1
                else:
                    cur.append(str(count)+pre[i-1])
                    count = 1
            cur.append(str(count)+pre[-1])
            pre = ''.join(cur)
        return pre


for pre in range(1, 20):
    print(pre)
    print(Solution().countAndSay(20, pre=str(pre)))
    print('\n')


"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 
1 <= n <= 30
generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.


Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
