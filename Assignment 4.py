class Person:
    def __init__(self, name, age,year):
       self.name = name
       self.age = age
       self.year=year

    def __str__(self):
        return f"NAME:{self.name}.\n Age:{self.age}.\n Year:{self.year}"
   
p1 = Person("John", 36,3)

print(p1)


"""
output:
NAME:John.
 Age:36.
 Year:3
 """

def list_operations(my_list):
    # Append an element to the list
    my_list.append(10)
    print("After appending 10:", my_list)
    
    # Remove an element from the list
    my_list.remove(5)
    print("After removing 5:", my_list)
    
    # Sort the list
    my_list.sort()
    print("After sorting:", my_list)
    
    # Reverse the list
    my_list.reverse()
    print("After reversing:", my_list)

# Example usage
my_list = [3, 6, 2, 8, 5]
print("Original list:", my_list)
list_operations(my_list)


"""
Output:
After appending 10: [3, 6, 2, 8, 5, 10]
After removing 5: [3, 6, 2, 8, 10]
After sorting: [2, 3, 6, 8, 10]
After reversing: [10, 8, 6, 3, 2]
"""
def student(name):
        
        if type(name) is str:
            return('invalid')
        
        else:
            return 'Hi '+ name
        
chat=student('ravi')
print(chat)

"""
output:
Hi ravi
"""

def worker(age):
      
      if type(age) is int:
             return 'my age was ' + age
      
      else :
             return'invalid datatype'
      
validation=worker('ravi')
print(validation)

"""Output:invalid datatype"""

def worker(age):
      if type(age) is int:
           return 'my age was ' + age
      
      try:
           age('hello')

      except(TypeError):
           print("something went wrong")

validation=worker('ravi')

"""Output:something went wrong"""

def student(year):
    return year + 12
try:
    student("ai@ds")
except (ValueError,TypeError):
    print("string and int doesnot Concatenation ?")

"""output:string and int doesnot Concatenation ?"""

def zeroerror(num):
    return num/0
try:
    zeroerror(10)
except(ZeroDivisionError):
    print(" any thing divided by zero is invalid ")


"""output:any thing divided by zero is invalid """


class Calculation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2 #Addition 15
    def sub(self):
        return self.num1-self.num2 #subraction 7
    def multi(self):
        return self.num1*self.num2 #mutiplication 144
    def div(self):
        return self.num1/self.num2 #Division 1.7777777777777777


performance=Calculation(16,9)
print("Addition",performance.add())
print("subraction",performance.sub())
print("mutiplication",performance.multi())
print("Division",performance.div())


''' output
Addition 25
subraction 7
mutiplication 144
Division 1.7777777777777777'''

def email_sent_by_student(name, age, year,college,department):

    return f"My name is {name} \n Hi I am {age} \n I Was studying { year}year\n From {college}\n And about my department {department}"

# You will get correct output because argument is given in order

print("Case-1:")
sent_to_mail=email_sent_by_student("Kalai", 20,3,"Annai mira college of engineering and technology","AI & DS")

print(sent_to_mail)

"""
My name is  Kalai
Hi, I am 20
I Was studying  3 year
From  Annai mira college of engineering and technology
And about my department AI & DS
"""

def bodmas(val_1,val_2):

    return val_1- val_2

val_1,val_2=80,20
result=bodmas(val_1,val_2)
print(result)                 

"""output :60"""


# defining pen class
class Pen():
     
	# args receives unlimited no. of arguments as an array
	def __init__(self, *args):
		# access args index like array does
		self.type = args[0]
		self.color = args[1]
          
# creating objects of pen class
parker = Pen('Ballpoint', 'red')
flair= Pen('Gell', 'black')
rorito= Pen('ink', 'white')

# printing the color and type of the pens
print(parker.color)
print(rorito.type)  

'''
output:
red
ink''' 


# defining Bag class
class Bag():
     
	# args receives unlimited no. of arguments as an array
	def __init__(self, **kwargs):
		# access args index like array does
		self.type = kwargs['s']
		self.color = kwargs['c']


# creating objects of Bag class
tycoon = Bag(s='laptop_bag', c='red')
f_gear = Bag(s='travel_bag', c='black')
baggit = Bag(s='school_bag', c='white')


# printing the color and type of Bag

print(f_gear.color)
print(baggit.type)

'''
output:
black
school_bag
'''

def week(n):
    match n:
        case 1 : return "sunday"
        case 2 : return "monday"
        case 3 : return "tuesday"
        case 4 : return "wednesday"
        case 5 : return "thursday"
        case 6 : return "friday"
        case 7 : return "saturday"
print(week(6))
print(week(7))

"""
output :
friday
saturday
"""

import  math
def area_of_circle (radius):
    area=math.pi*radius*radius
    return area
print ("Area of circle",area_of_circle(15))
        
"""Area of circle 706.8583470577034"""

import  math
def distance(val_1,val_2):
    """val_1=(2, 3)
    val_2= (5, 7)"""
    distance_of_two=math.dist(val_1, val_2)
    return distance_of_two
print ("Distance between two points",distance((2, 3),(5, 7)))
        
"""Distance between two points 5.0"""

from datetime import date
# date object of today's date
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

"""
output:
Current year: 2024
Current month: 3
Current day: 17"""

import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

""" output  : ['apple', 'cherry', 'banana']"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

""" output:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]"""
