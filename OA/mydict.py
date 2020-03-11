from collections import OrderedDict

class MyDict(dict):
    """
    How would you design a class that behaves similar to a Java Map 
    <Date,Object> except that get() returns the mapped value 
    if an exact match is present
    the mapped value of the closest previous Date in the Map 
    if an exact match is not present
    null if there is no Date in the Map less than 
    or equal to the requested Date
    Implement the get() and put() methods of the class.

    """
    def __init__(self):
        pass
    
    def get(self):
        pass
    
    def put(self):
        pass
    
    

d = MyDict()
d[0] = 1
print(d)

