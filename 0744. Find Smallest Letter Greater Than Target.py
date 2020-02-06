# binary search, time O(log(n)), space O(1)
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters or not ('a' <= target <= 'z') \
        or (letters[0] == letters[-1] == target):
            return ""
        if letters[-1] <= target:
            return letters[0]
        
        left, right = 0, len(letters)-1
        while left + 1 < right:
            mid = left + (right-left)//2
            if letters[mid] > target:
                right = mid
            else:
                left = mid
        if letters[left] > target:
            return letters[left]
        elif letters[right] > target:
            return letters[right]
        else:
            return letters[0]
        



# time O(n), space O(1)
class Solution1(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters or not ('a' <= target <= 'z'):
            return ""
        res = float('inf')
        for c in letters:
            num = (26 + ord(c) - ord(target))%26    # shift all letters so that target is set to 0
            if num > 0:
                res = min(res, num)
        code = res + ord(target)
        if code > ord('z'):
            code -= 26
        return chr(code)


"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""
