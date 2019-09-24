# time O(m+n)
from collections import defaultdict
class Solution(object):
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
        window, goal = defaultdict(int), defaultdict(int)
        
        # save letters of t in a dictionary, goal = {letter:cnts}
        for letter in t:
            goal[letter] += 1

        # set left, right at 0
        left, right = 0, 0
        cnt = 0  # number of letters of t that are found
        
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
    
