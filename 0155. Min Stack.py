# similar questions: max stack, median stack (use heap)

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.nums.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.nums:
            return
        x = self.nums.pop()
        if x == self.mins[-1]:
            self.mins.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.nums:
            return None
        return self.nums[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.mins:
            return None
        return self.mins[-1]
        
            

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
