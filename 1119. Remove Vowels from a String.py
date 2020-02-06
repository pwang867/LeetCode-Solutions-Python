class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = [c for c in S if c not in {"a", "e", "i", "o", "u"}]
        return "".join(res)


import re
class Solution2(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        return re.sub("a|e|i|o|u", "", S)


class Solution1(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        return S.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
    
"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""
