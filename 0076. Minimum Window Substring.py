# same as method 1, but the logic is more clear and easier to explain
# time O(m+n)
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        window = Counter(t)
        min_len = float('inf')
        subseq = ""
        
        right = 0
        cnt = 0
        for left in range(len(s)-len(t)+1):
            # move right pointer till the window contains t
            while right < len(s) and cnt < len(t):
                if s[right] in window:
                    window[s[right]] -= 1
                    if window[s[right]] >= 0:
                        cnt += 1
                right += 1
                if cnt == len(t):
                    break
            # update results
            if cnt == len(t):
                if right - left < min_len:
                    min_len = right - left
                    subseq = s[left:right]
            # update left
            if s[left] in window:
                window[s[left]] += 1
                if window[s[left]] > 0:
                    cnt -= 1
        
        return subseq



# time O(m+n)
from collections import defaultdict
class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # edge cases
        if not t or not s:
            return ''
        
        # initializing
        min_width = float("inf")
        substring = ""
        goal = defaultdict(int)
        # save letters of t in a dictionary, goal = {letter:cnts}
        for letter in t:
            goal[letter] += 1

        # set left, right at 0
        left, right = 0, 0
        cnt = 0  # number of letters of t that are found
        window = defaultdict(int)
        for right, letter in enumerate(s):
            if letter in goal:
                # keep track of the letter between left and right 
                # that appeared in goal = {letter: cnts}
                window[letter] += 1
                if window[letter] <= goal[letter]:
                    cnt += 1
            # if all letters in t are found, stop scanning:
            if cnt == len(t):
                # keep moving left pointer to shrink the window
                # making sure letters between left and right still contains t
                while cnt == len(t):
                    # print "test1", left, right, cnt, window, goal
                    if s[left] not in goal:
                        left += 1
                    elif goal[s[left]] < window[s[left]]:
                        # the order of those two sentences are important !!!
                        window[s[left]] -= 1  
                        left += 1
                    else:
                        break
                # check length of the window, update the min_width
                window_size = right - left + 1
                if window_size < min_width:
                    min_width = window_size
                    substring = s[left:right + 1]

        # return min_width
        return substring

"""
Given a string S and a string T, 
find the minimum window in S which will contain 
all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that 
covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that 
there will always be only one unique minimum window in S.
"""
