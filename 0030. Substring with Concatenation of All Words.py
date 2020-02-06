# time O(k*n), k=len(words[0]), n = len(s), sliding window
# start from i (0<i<k-1), and then slice s from i, i+k, i+2*k, i+3*k, ...
# ehn we can use a sliding window to compare with words within O(n)
# in this way, we don't have to slice the string s again and again 
# starting from i+k, i+2*k, ... and thus reducing time

# similar to: 76. Minimum Window Substring
# and 3. Longest Substring Without Repeating Characters
# ref: https://blog.csdn.net/linhuanmars/article
# /details/20342851?utm_source=tuicool&utm_medium=referral
from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1
        
        res = []
        n = len(words)
        k = len(words[0])
        for i in range(k):
            blocks = [s[j:j+k] for j in range(i, len(s)-k+1, k)]
            self.slidingWindow(blocks, word_dict, res, i, n, k)
        
        return res
    
    def slidingWindow(self, blocks, word_dict, res, i, n, k):
        left, right = 0, 0
        cnt = 0
        window = defaultdict(int)
        while right < len(blocks):
            if blocks[right] not in word_dict:  # reset all parameters
                window.clear()
                left = right + 1
                right += 1
                cnt = 0
            else:
                window[blocks[right]] += 1
                if window[blocks[right]] <= word_dict[blocks[right]]:
                    cnt += 1
                else:
                    while window[blocks[right]] > word_dict[blocks[right]]:
                        window[blocks[left]] -= 1
                        if window[blocks[left]] < word_dict[blocks[left]]:
                            cnt -= 1
                        left += 1
                if cnt == n:
                    res.append(i+left*k)  # mistake: res.append(left*k)
                    window[blocks[left]] -= 1
                    cnt -= 1
                    left += 1
                right += 1




from collections import defaultdict
from copy import copy
# time O(n*m*k), space O(m*k), n=len(S), m=len(L), k=len(L[0])
class Solution1:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):        
        if not S or not L:
            return []
        
        n = len(S)
        m = len(L)  # number of words
        k = len(L[0])  # word length
        ans = []
        
        _dict = defaultdict(int)
        for word in L:
            _dict[word] += 1
        
        for i in range(n - k*m + 1):
            temp_dict = copy(_dict)
            for j in range(m):
                temp_word = S[i+j*k: i+j*k+k]
                temp_dict[temp_word] -= 1
                if temp_dict[temp_word] < 0:
                    break
            else:
                ans.append(i)
        
        return ans


"""

You are given a string, s, and a list of words, words, 
that are all of the same length. 
Find all starting indices of substring(s) in s 
that is a concatenation of each word in words exactly once 
and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

"""

