# invalid IP: 255.01.1.1
# IP number range: [0, 255]
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.helper("", s, 1)
        return self.res
        
    def helper(self, path, s, i):
        # s: str, the left over string
        # i: to search i-th number in IP
        
        # base case condition
        if len(s) == 0:
            return
        
        if i == 4:
            if int(s) <= 255:
                if s[0] == "0" and len(s) > 1:
                    return
                self.res.append((path + "." + s)[1:])
            return
            
        for j in range(3):  # at most 255
            if int(s[:j + 1]) <= 255:
                if s[0] == "0" and j > 0:  # wrong: 255.01.1.1
                    break
                x = self.helper(path + "." + s[:j+1], s[j+1:], i+1)
            else:
                break

"""
Given a string containing only digits, restore it by returning all possible 
valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
