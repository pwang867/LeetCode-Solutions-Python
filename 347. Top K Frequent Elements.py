# method 4: bucket, space O(n), time O(n)
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.Counter(nums)
        
        buckets = [[] for i in range(len(nums)+1)]
        for num, freq in d.items():
            buckets[freq].append(num)  # bucket index is frequency
            
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

# # method 1, 2, 3
# import collections
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         d = collections.Counter(nums)
        
        
#         return self.extractTopK(d, k)
    
#     def extractTopK(self, d, k):
#         """ extract the most common k keys in the dictionary d"""
        
#         # method 1: use Counter.most_common(), time: O(n+k*log(n))
#         # Counter.most_common() will call heapq.nlargest(), space: O(k)
#         # pairs = d.most_common(k)
#         # res = [key for key, value in pairs]
        
#         # method 2: use sort(), O(n*log(n))
#         # pairs = [(key, value) for key, value in d.items()]
#         # pairs.sort(key=lambda x: x[1], reverse=True)
#         # res = [pair[0] for pair in pairs[:k]]
        
#         # method 3: use min Heap, O(n+k*log(n)), space: O(k)
#         res = heapq.nlargest(k, d.keys(), key=lambda x: d.get(x))
        
#         return res
