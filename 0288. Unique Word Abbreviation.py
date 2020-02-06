# edge case: dictionary = ["cake"], word = "cake", return True
from collections import defaultdict
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbs = defaultdict(set)
        for word in dictionary:
            abb = self.abbreviate(word)
            self.abbs[abb].add(word)
    
    def abbreviate(self, word):
        if not word:
            return ''
        if len(word) < 3:
            return word
        return word[0] + str(len(word)-2) + word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abb = self.abbreviate(word)
        if abb not in self.abbs:
            return True
        else:
            return len(self.abbs[abb]) == 1 and word in self.abbs[abb]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

"""
Share
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
A word's abbreviation is unique if no other word from the dictionary 
has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
isUnique("cake") -> true
"""
