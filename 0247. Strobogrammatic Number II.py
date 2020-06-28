# recursion, time O(n*len(res))


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        path = [""]*n
        d = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        res = []
        self.helper(path, 0, d, n, res)
        return res
    
    def helper(self, path, i, d, n, res):
        if i == n//2:
            if n % 2 == 0:
                res.append("".join(path))
            else:
                path[n//2] = "0"
                res.append("".join(path))
                path[n//2] = "1"
                res.append("".join(path))
                path[n//2] = "8"
                res.append("".join(path))
            return
        for num in d:
            if i == 0 and num == "0":
                continue
            path[i] = num
            path[-i-1] = d[num]
            self.helper(path, i+1, d, n, res)


# iteration, time O(n*len(res))
class Solution1(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairs = (('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6'))
        if n%2 == 0:
            ans = ['']
        else:
            ans = ['0', '1', '8']  # not ['0', '1', '6', '8', '9']
        if n <= 1:
            return ans
            
        for i in range(n/2):
            new_ans = []
            for num in ans:
                for pair in pairs:
                    if i == n/2 - 1 and pair == ('0', '0'):
                        continue
                    new_ans.append(pair[0] + num + pair[1])
            ans = new_ans
        
        return ans

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""
    