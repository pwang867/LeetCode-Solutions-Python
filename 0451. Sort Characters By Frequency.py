# method 2: use buckets, time O(n), space O(n)
import collections
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
# import collections
# class Solution(object):
#     def frequencySort(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         d = collections.Counter(s)
#         pairs = d.most_common()  # a list of (key, value) pairs
#         res = []
#         for letter, freq in pairs:
#             res.append(letter*freq)
#         return "".join(res)
    
