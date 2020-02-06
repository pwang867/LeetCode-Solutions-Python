# time O(n), space O(res)
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        keyboard = {}  # letter: row
        for i, row in enumerate(["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]):
            for c in row:
                keyboard[c] = i
        res = []
        for word in words:
            if not word:
                continue
            row = keyboard[word[0].upper()]    # watch out upper case and lower case
            for c in word:
                if keyboard[c.upper()] != row:
                    break
            else:
                res.append(word)
        return res


"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

 



 
Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
