# 2016-8-24 Python lessons from Coursera
# In Python, WHITESPACE is used to structure code.
# You should indent your code with FOUR SPACES.
# Python 不识别单引号和双引号
# cd C:\Python27>python fruits.py #怎么运行程序
"""for multi-line comments, you can include the whole block in a set of triple quotation marks"""
#Modifying an element in a list in a function is the same as if you were just modifying an element of a list outside a function.

5 / 2 # 2
5.0 / 2 # 2.5
float(5) / 2 # 2.5

for item in list:
    print item

for i in range(len(list)):
    print list[i]
	
for number in range(5):
	print number,

d = { "name": "Eric", "age": 26 }
for key in d:
    print key, d[key],

for letter in "Eric":
    print letter,  # note the comma!


def spam():
    eggs = 12
    return eggs
    
print spam()

spam = True
eggs = False

10**2 # 指数
spam = 5 % 2 # modulo

caesar = "Graham"
praline = "John"
viking = "Teresa"

#Three ways to create strings
'Alpha'
"Bravo"
str(3)

# In Python, we start counting the index from zero instead of one.
#Python中的print必须全部小写
#for strings
len()
lower()
upper() #string.upper()并不改变string
str()

len("Charlie")
"Delta".upper() # dot operators are only for strings, 但是并不改变string本身
"Echo".lower()

parrot = "Norwegian Blue"
print parrot.lower()

#Methods that use dot notation only work with strings.
#concatenation：print "Life " + "of " + "Brian"
print "I have " + str(2) + " coconuts!"

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")
print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." %(name, quest, color)

my_string = "I love Ariel!"
print len(my_string)
print my_string.upper()

from datetime import datetime
now = datetime.now()
print now
print now.year
print now.month
print now.day
print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)

#comparators: ==, !=, <, <=, >, >=
boolean operator: and, or, not (顺序：not, and, or)

def the_flying_circus():
    if (8 < 7):    # Don't forget to indent #Don't forget to include a : after your if statements!
        return False
    elif 8 == 7:
        return False
    else:
        return True
print the_flying_circus()

x = "J123"
x.isalpha()  # False

def spam():
    """Prints 'eggs!' to the console"""
    print "Eggs!"
spam()

from math import sqrt
from module import *


import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

print type(12)
print type(2.3)
print type("string")

def distance_from_zero(number):
    if type(number) == int or type(number) == float:
        return abs(number)
    else:
        return "Nope";
		
		
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city == "charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

		
#taking a vacation
def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)
        
assignment statement: z=1


animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]      # The fourth through sixth characters
frog = animals[6:]  # From the seventh character to the end

animals = ["ant", "bat", "cat"]
animals.index("bat")
animals.insert(1, "dog")

my_list = [1,9,3,8,5,7]
for number in my_list:
    print 2 * number
	
# .sort() modifies the list rather than returning a new list.
animals = ["cat", "ant", "bat"]
animals.sort()

start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
    square_list.append(number ** 2)
square_list.sort()

#dictionary
d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin'] # Prints Puffin's room number
del d['key1']

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
beatles.pop(1) #removes item of index 1, and then print the removed item
del(beatle[1]) #remove index 1 but doesn't print


my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]


#practice for python list and dictionary
inventory = {
    'gold' : 500, #一定要用逗号
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print my_dict.keys()
print my_dict.values()
print my_dict.item() #output tuples

#Note that dictionaries are unordered, meaning that any time you loop through a dictionary, you will go through every key, but you are not guaranteed to get them in any particular order.

for letter in "Codecademy":
    print letter

#shopping list
shopping_list = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}  
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total
compute_bill(shopping_list)

range(stop)
range(start, stop)
range(start, stop, step)


#lists in lists in a functionn = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results
print flatten(n)

from random import randint
letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)

	
import random
print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"
count = 0
while count < 3: 
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break # If the loop exits as the result of a break, the else will not be executed.
    count += 1
else:
    print "You win!"

break #If you are using nested loops, the break statement stops the execution of the innermost loop and start executing the next line of code after the block.	
	
choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
    print index +1, item

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b): #zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
    print max(a,b)

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

floor divide: //

def reverse(text):
    list_text = []
    text = str(text)
    n = len(text)
    for i in range(n):
        list_text = list_text + [text[i]]
    rev_text = []
    for i in range(n):
        rev_text = rev_text + [list_text[n-1-i]]
    rev_text = "".join(rev_text)
    return rev_text
	
def reverse(text):
    n = len(text)
    new_list = ""
    while n > 0:
        new_list = new_list + text[n-1]
        n = n - 1
    print new_list
    return new_list

"a" in "aeiouAEIOU" #True

x="abc"
print x[1] # "b"

d = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True
}
print d.items() # the items() function doesn't return key/value pairs in any specific order.

# list comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]
# => [6]

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]

letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1] #print out ['E', 'D', 'C', 'B', 'A'].

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

squares = [x**2 for x in range(1,11)]
print filter(lambda x: x > 30 and x < 70, squares)

print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

In Python, you can write numbers in binary format by starting the number with 0b. 
When doing so, the numbers can be operated on like any other number!
print bin(5) #0b101
print int("11001001",2)
print bin(0b1110 | 0b101)

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

#mask
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

# ^ is used to flip every bit of a number with a mask
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)

class Fruit(object): #By convention, user-defined Python class names start with a capital letter
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."
lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()

Class Scope

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."
my_cart = ShoppingCart("Weimin")
my_cart.add_item("Apple", 1.54)



# class override
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    

class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False 
my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()


class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, str(self.mpg))
    
    def drive_car(self):
        self.condition = "used"
my_car = Car("DeLorean", "silver", 88)
print my_car.condition  #new
my_car.drive_car()
print my_car.condition   #used

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" %(self.x, self.y, self.z)
my_point = Point3D(1,2,3)
print my_point  #(1,2,3)


"""input and output files"""
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10
f = open("output.txt", "w")  #"w" stands for "write", "r+" for read and write
for item in my_list:
    f.write(str(item) + "\n") #The write() function takes a string argument
f.close()
"""You can open files in write-only mode ("w"), read-only mode ("r"), 
read and write mode ("r+"), 
and append mode ("a", which adds any new data you write to the file to the end of the file)."""

my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

with open("text.txt", "w") as textfile:
	textfile.write("Success!")

f = open("bg.txt")
f.closed # False, "closed" is an attribute
f.close()
f.closed # True

a = [1,2,3,4]
c=a*2; 
print c #[1, 2, 3, 4, 1, 2, 3, 4]
numpy.mean(a)


import numpy as np
data1 = np.random.normal(0, 1, size=50)
data2 = np.random.normal(2, 1, size=50)
