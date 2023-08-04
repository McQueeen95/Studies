###Coding
# x = input() here x will hava data type string as it auto takes the input as string , if we want to take integer : int(input())
# in python there is no concatenation just str on int
# x = input() //5 this is str
# y = input() //3.0 this is str
# print(x + y) //53.5 # and this wrong to make it right we use int(input())
# (True , False , < , > , == , <= , >= ,!=) is comparison operations
# (and , or , != ) is logical operations
#  == can compare 2 strings
# x**2 (this x square)
#
#
#########################################################################
# x = float(input())
# y =str( x + x*0.25)
# print("the amount of x is : " + y)
#########################################################################
# x = 9
# y = 10
# c = x//y #this will result an float 0.0 number || for integer result we use x // y (Floor Division: round down to the closest integer)
# print(c)
# print(type(c)) # here we found what happen is (implicit data type conversion) because data type changed automatically during execution
# print(float(x))# here(explicit data type conversion) because I'm the one who changed the data type explicitly
#########################################################################
# print (5!=3 != 6>5) # not like others , and sign is ("and")
# print (True or False) # the same here or sign is ("or")
# print (True != False)
#########################################################################
# for i in range(3): #here the itration will be in range from 0 to 2 or 0 to (n-1)
#     print(i)
# for _ in range(3,11,2): #here the itration will be in range from 3 to 10(n-1) and jumping 2 numbers
#     print(_) # we can use ( _ ) as a one time variable
#     print("I'm in the loop") #here i used 2 taps , I can use number taps i want just is must be consistent
# print("I'm not") #the code that gets repeated must be indented (at the same space of the beginning of lines)
# i = int(input())
# while i >= 0 :
#     print(i)
#     i -= 1
#########################################################################
# x = 5
# button = False
# if x > 2 or button:
#     print("hi bro ")
#     print("this inside the if")
# else:
#     print("this else")
# print("this outside the if else")
# x = int(input("Enter your Glucose level: "))
# if x < 70:
#     print("Low glucose level")
# elif x > 140:
#     print("High glucose level")
# else:
#     print("Normal range")
#########################################################################
# Data Stuctures(Strings, Lists , Dictionaries , Tuples , Sets)
###Lists
# x = [1,5,'A',"HI",True,[1,2,3]] # Lists is like Arrays
# print(x[5][1])
# print(x[3][1])
# y = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#     ]
# print(y[2][1]) #y[row][col]
# print(input()[2]) #this used only for strings
# =================================
##List operations
# ==============
# x = [2,4]
# x += [6,8] # x = [2,4,6,8]
# print(x[2])
# x[2]=5
# print(x[0])
# print(x[2]/x[0])
# ==============
# x = [1,2,3]
# print(x*3) # repeating the list or string by 3(integer) not for math op
# print(x+[4,5,6]) #concatenate
# y = "ahmed"
# print(y*3) # including new list or string to existing list
# ==============
# x = ["hi" , "bro", "how", "you" , "doin" , 6]
# y = "Hello, world"
# print("hi" in x)
# print(5 in x)
# print(x)
# if not 5 in x:
#     print("good")
# else:
#     print("bad")
# if "He" in y:
#     print("ns")
# ==============
# words = ["hi" " my name" " is" " ahmed"]
# nums = [4,7,3,1]
# str = "Hello mona , what ever happen u r my solemate"
# countOfSpaces = 0
# for x in nums:
#     print(x*2)
# for s in str:
#     if s == " ":
#         countOfSpaces += 1
# print(countOfSpaces)
# we can use break to break and exit from the loop , and use continue to jumb to next iteration
# ==============
# range() function
# we can use it in 2 ways
# First:
# for _ in range(5):
#     print(_)  # 0  1  2  3  4
# Second:
# x = range(5) # this line only output is: range(0,5)
# print(list(x))# here we convert the range into a list [0,1,2,3,4]
# print(*list(range(2,6))) # this output the range without [] or , # and * removes brackets
# print(*list(range(2,6)),sep='-') # this output the range without [] but with - as a sep
# print(range(4) == range(0,4)) # this returns true
# print(list(range(3,9))) # this produce a list from 3 to 8 **range(start,end) => [start,....,end-1]
# print(list(range(3,9,2))) # this produce a list from 3 to 8 jumbing 2 numbers **range(start,end,steps) => [start,start+2,....,(end-2 || end -1)]
# so from all we notice that : range(5) == range(0,5) == range(0,5,1)

# note that we dont use floats in range funciton  (but we can make it in egyption ways xD)
# nums = list(range(0 , 10 , 0.5)) => error
# nums = list(range(11))
# newNum = []
# for i in nums:
#     newNum.append(i*0.5)
# print(newNum) # this code print from 0.0 to 5.0
# print(list(range(6,2,-1))) # we can use it to go backwards
# ==============
## List Slices
# x = [0,1,2,3,4,5,6,7,8,9,10]
# y = x[0:2] # returns a new list containing all the values between the indices(except the end)
# z = x[0:1] # retrun [start , ....., end-1]
# t = x[:3] # the same but its starts from 0 index by defualt
# print(y)
# print(z)
# print(x[:4]) # prints all before 4th element
# print(x[4:]) # prints 4th element and all after it
# print(x[:] == x[0:] and x[:] == x[::]) # all the same
# print(x[::2]) # prints from the first to last element by jumping 2 steps
# print(x[4:9:2])
# print(x[6:-2]) # when use -ve valus its mean that we count from last index
# print(x[6:-2] == x[6:9])
# print(x[9:5:-1]) #when use -ve valus at steps it starts from the end as[start from end , end from first , steps]
# print(x[::-1]) # popular way to reverse a list
# print(x[-1:]) #prints last value  in the list
# y = [0,1,2,3,4]
# print(y[1:-1])
# x = input()
# print(x[-1:]) # takes string and retruns the last character
# ===============================================================================
## Functions
# List methods
# x = [12,34,54,65,3,6,4,"ahm"]
# print(len(x)) #return the length of the list
# x.append("hi") # adding at the end
# x.clear() # removes all the elements from the list
# y = x.copy() # returns a copy
# print(x.count(12)) # returns the count of specified element
# y=[1] ; y.extend(x) # takes from list to another at the end ;print(y)
# print(x.index(34)) # returns index of the first element
# x.insert(2,"3rd place") # adds an element at the specified index
# x.pop(2) # removes the element at the specified index
# x.remove(34) # removes the first object with the specified object
# x.reverse() # reverse the order of the list
# x.sort() # sort the list
# print(max(x)) # returns the max value
# print(min(x)) # returns the min value

# 3 ways of formating
# a = "abra"
# b = "cad"
# print("%s%s%s"%(a,b,a)) #old way
# print("{0}{1}{0}".format(a,b)) #new way
# print(f"{a}{b}{a}") #new way

# =================================================
# how to make function

# def funcName():
#   print("hi i'm function")

# funcName()

# search engine problem
# take two inputs (text , word(search for it in the text))

# def search(text,key):
#   textList = text.split(" ")
#   for _ in range(len(textList)):
#     if textList[_] == key:
#       return "Word found"
#   return "Word not found"

# print(search(input(),input()))
# =================================================
# List [] mutable
# Tuple() immutable
# Dictionary{key:value} mutable
# Set {} or {[]} mutable
# =================================================
# ## Dictionary
# dicName = {
#   "key" : value,
#   "key1" : value,
# }
# ages = {"dave": True, "mary": 34, "john": 58}  # way 1
# ages2 = {
#   "Dave":36,
#   "mary":15,
#   "john":37
# } # way 2
# print(ages["dave"])
# print(ages2["Dave"])
# nums = {1: "one",
#         2: "two",
#         3: "three"
#         }
# print(1 in nums) # return true if we have key = 1
# print("one" in nums) # return false because its not key (its a value)
# print(4 not in nums) # return true as key 4 not in nums
# so in function is only for keys
# pairs = {
#   1:"apple",
#   "orange" : [2,3,4],
#   True : False,
#   12 : "True"
# }
# print(pairs.get("orange")) # getting the value of "orange" key
# print(pairs.get(7,42)) # same but if key 7 not here its prints 42
# print(pairs.get(12345,"not found"))  # same but if key 12345 not here its prints "not found"
# =================================================
## Tuple
# x = ("ahmed" , "mohamed" , "ibrahem")
# y= "1" , "2" , "3"
# print(x[0])
# print(type(y[1]))

# search key problem
# def search(searchKey):
#   contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
#   for i in range(len(contacts)):
#     if searchKey == contacts[i][0]:
#       return f"{contacts[i][0]} is {contacts[i][1]}"
#   return "Not found"
# print(search(input()))

# another solution
# contacts = [ ('James', 42), ('Amy', 24), ('John', 31), ('Amanda', 63), ('Bob', 18) ]
# contacts = dict(contacts)
# name = input()
# if name in contacts: print(name, "is", contacts[name])
# else: print("Not Found")

# swap values
# a , b = 4 ,5
# print(f"{a} and {b}")
# a , b = b , a # swapping
# print(f"{a} and {b}")

# a , b , *c , d = [1,2,3,4,5,6,6,7] # * means unpack rest of elements to the c
# print(f"{a} {b} {c} {d}")
# ============================================================
## sets (non repeatable elements && non invoking each of elements(not indexed) && ordered elements)
# Nset = {6,4,5,9}
# print(Nset)
# print(3 in Nset) # check if 3 is in the set
# Nset.add(1)
# Nset.remove(9)
# first = { 2 ,4 ,6 , 5 , 8 ,0}
# second = { 1 ,3 ,5 ,7 , 0 ,9}
# print(first  | second) # union U
# print(first  & second) # intersectioin ∩
# print(first  - second) # elements that exists in first and not in second (difference)
# print(second - first) # elements that exists in second and not in first
# print(first ^ second) # (gets items in either set but not both) (symmetric difference)
# x = {"html","css","javascript"}
# y = {"html","aa","bb"}
# print(" ".join(x & y))
# print(*(x & y)) # we put * to unpack it so it be a normal string not a set element
# ============================================================
## List Comprehensions (creating a lists whose contents obey a rule)
# [x | P(x)] this means : x such that x is some polynomial or some function
# cubes = [i**3 for i in range(5)]
# print(cubes)
# instead of typing 0 to 100 in a list we may use this:-
# ls = [x for x in range(101)]
# print(ls[100])
# we can add a condition to this list:-
# evens = [i for i in range(11) if i % 2 == 0]
# print(evens)
# ============================================================
# summary (Lists , Dictionaries, Tuples , Sets)
# use Dictionaries when :
#   1) need a logical association between a key:value pair
#   2) fast lookup for you data based on a custom key
#   3) modifiy data constantly as its mutable
# use Lists when :  1) having collection of data that does not need random access (simple iterable collection that is modified frequently)
# use Set when :    1) need uniqueness for the elements (non repeataple)
# use Tuples when : 1) data can't and shouldn't change
# ============================================================
### functions
# def adding(x,y):
#   return x + y
# print(adding(5,6))
## Functional Programming (takes other functions as arguments or return them as results)
# def apply3Times(func , num):
#   return(func(func(func(num))))
# def add5(x):
#   return (x+5)
# print(apply3Times(add5,20))
## Pure and Impure functions
# def pureFunction(x,y):
#   t = x + 2*y
#   return t / (2*x + y) # its pure because it doesn't effect other variables (x and y still the same)

# ls = []
# def impureFunction(x):
#   ls.append(x) # not pure as it changes a variable outside of the function
# note :- memoization is the reducing the number of times the function called by caching the results of fuction calls
# as the output is stored in a cache if the function is called again with the same input , the cached output is returned instead of recalculating the functoin

## Anonymous Function (on-the-fly function)
# lambda
# print((lambda arg: expression)(value))
# def myFunc(f,arg):
#   return f(arg)
# print(myFunc(lambda x: 2*x*x , 5))

# def poly(x):         #namedFunction
#   return x**2 + 5*x + 5
# print(poly(-4))
# print((lambda x: x**2 + 5*x + 5)(-4))             #lambda function
# print((lambda x,y: x+y)(2,3))
# ============================================================
## map (built in function that operate on lists or any iterables and returns a new iterable(not a list or something))
# ls = [3,5,64,64,43,26]
# def add4(x):
#   return x + 4
# rs = map(add4,ls) # return a map opject(iterable)
# rs1 = list(map(add4,ls))
# print(rs1)
# print(list(map(lambda x: x+4,ls))) # using two ways of creating functions

## problem
# def func(ls,bs):
#   for i in range(len(ls)):
#     ls[i] = ls[i] + bs
#   return ls  ### way 1 to solve
# bonus = int(input())
# def addBouns(x):
#   return x + bonus ### another way
# salaries = [2000, 1800, 3100, 4400, 1500]
# print(list(map(addBouns,salaries)))
# print([x+bonus for x in salaries])
# print(list(map(lambda x: x +bonus , salaries)))
## filter
# nums = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x%2==0, nums))
# print(res)
# ============================================================
### Generators (its iterable but don't allow indexing and can be iterated with for loops >> using yield statment)
# its used to loop over many amount of data without storing it
# it don't have the memory restrictions like lists >> it can be infinite!
# Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
# def gen(n):
#   for i in range(n):
#     yield i # here its go to return the current value and get back to complete the loop
# print(gen(5)) # this return generator object not alist
# print(list(gen(5))) # this list of this generator
# x = gen(4)
# print(next(x))
# print(next(x))
# print(next(x))
# def gen1():
#   yield 1
#   print("pause1")
#   yield 2
#   print("pause2")
#   yield 3
#   print("pause3")
#   yield 4
# x = gen1()
# print(next(x))
# print(next(x))
# print(next(x))
## Generators Comprehensions
# x = (i**2 for i in range(6)) # this is a generator
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))

# problem
# def isPrime(x):
#     if x < 2:
#         return False
#     elif x =0= 2:
#         return True
#     for i in range(2, x):
#         if x % i ==0:
#             return False
#     return True
# def primeGenerator(a, b):
#   for i in range(a,b):
#     if isPrime(i):
#       yield i
# f = int(input())
# t = int(input())
# print(list(primeGenerator(f, t)))
# ============================================================
# Decorators (when one function is used to modify another function.)
# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.
# # Example
# def mainFunction():
#   print("Hello,World")
# def functionModifiy(func):
#   print("========")
#   func()
#   print("=======")
# functionModifiy(mainFunction)

# # Example 2
# def decor(func):
#   def wrap():
#     print("========")
#     func()
#     print("=======")
#   return wrap
# @decor
# def prnTx():
#   print("Hello")
# prnTx()

# # Example 3
# def invoice(num):
#     print("INVOICE #" +num)

# def decor(func,x):
#   print("***")
#   func(x)
#   print("***")

# decor(invoice,input())
# ============================================================
# Recursion
# Ex1
# def rec(x):
#   if x==1:
#     return 1
#   return x*rec(x-1)
# print(rec(5))
# Ex2
# def is_even(x):
#   if x == 0:
#     return True
#   else:
#     return is_odd(x-1)
# def is_odd(x):
#   return not is_even(x)
# print(is_odd(2))
# print(is_even(1))
# Ex3
# def convert(num):   # converts from decimal to binary
#   if num == 1:
#     return 1
#   return num % 2 + 10 * convert(num // 2)
# print(convert(7))
# ============================================================
# # *args
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
# The arguments are then accessible as the tuple args in the body of the function.
#  it collects any extra positional arguments passed to the function into a tuple.
# Ex1
# def function(named_arg, *args):   #Just remember that 'args' is the NAME of the tuple while '*args' is the WAY TO LET THE COMPUTER KNOW that a function has a dynamic number of arguments
#     print(named_arg)
#     print(args)
# function(1, 2, 3, 4, 5)
# a , *d , e =[1,2,35,66,34,33] # this here called args
# print(f"{a} , {d} , {e}")
# Ex2
# def my_function(*args):
#     for arg in args:
#         print(arg)
# my_function("apple", "banana", "cherry")        # In this example, the function my_function takes any number of arguments, and *args collects them into a tuple named args. 
# my_function(1,2,3,4,5,6,6,7,7,7,3,52,354,45)    # You can then iterate over args or perform any other operations on the arguments.
# Ex3
# def my_min(*args):
#     return min(args)
# print(my_min(8, 13, 4, 42, 120, 7))
# # **kwargs
# The **kwargs parameter allows a function to accept any number of keyword arguments. 
# It collects any extra keyword arguments passed to the function into a dictionary.
# Ex1
# def my_function(**kwargs):
#     for key, value in kwargs.items():   # In this example, the function my_function takes any number of keyword arguments, and **kwargs collects them into a dictionary named kwargs.
#         print(key, value)               #  You can then access the keyword arguments as key-value pairs in the kwargs dictionary.
# my_function(name="John", age=25, city="London")
# Ex2
# def my_func(x, y=7, *args, **kwargs):
#     print(kwargs)
#     print(x)
#     print(y)
#     print(args)
# my_func(2, 3, 4, 5, 6, a=7, b=8)
# Both *args and **kwargs provide flexibility in function definitions by allowing you to handle a variable number of arguments.
# You can use them together in a function definition if you need to accept both positional and keyword arguments.
### Quiz
# nums = [1,2,8,3,7]
# x = list(map(lambda x:x%2==0,nums)) # here its maps on the list and check from the expression and return if true of false
# print(x)
# nums1 = [1,2,8,3,7]
# x1 = list(filter(lambda x:x%2==0,nums)) # here its use the expression to filter the list 
# print(x1)