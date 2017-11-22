print "hello"
print "hello world"
import math
x=math.exp(0)
print x


name = raw_input('please enter your name: ')
print 'Hello,', name


classmates = ['Michael', 'Bob', 'Tracy']
classmates[-1] # 'Tracy'

len(classmates)
classmates.append('Adam')
classmates.insert(1, 'Jack')
classmates.pop() # 要删除list末尾的元素用pop()方法
classmates.pop(1) # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置

L = ['Apple', 123, True] #list里面的元素的数据类型也可以不同

#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
t = (1,) #只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：


