# good for practicing yield

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        characters = list(characters)
        self.it = self.dfs(characters, 0, [], combinationLength)
        self.buffer = next(self.it) if characters else None
        
    def dfs(self, characters, start, path, combinationLength):
        if len(path) == combinationLength:
            yield "".join(path)    # code after yield will still be run
        else:  
            for i in range(start, len(characters)+ 1 - (combinationLength - len(path))):
                path.append(characters[i])
                for x in self.dfs(characters, i+1, path, combinationLength):
                    yield x
                path.pop()

    def next(self):
        res = self.buffer
        try:
            self.buffer = next(self.it)
        except:
            self.buffer = None
        return res
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buffer != None


"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
"""
