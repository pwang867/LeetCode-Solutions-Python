#问题
#怎样用python自动发QQ说说
#怎样用python来发表情


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


age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
	
	
range(5) #[0, 1, 2, 3, 4]

sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

birth = int(raw_input('birth: '))#raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型：

强制结束Python进程: Ctrl+C
