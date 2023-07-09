# studying
# Free and open Source
# Iterpreted(not compiled) : no need to compile because its process in runtime
# interactive
# integrated
# support module and packages
# large set of libs and plugins
# Data is stored
# data structure in python :-
# int(Integer)
# float(Floating point number)
# str(String)
# list([1,2,3])
# tuple( (1,2,3) )
# dict (Dictionary) => ({"one":1, "Two":2, "Three: 3"})
# boolean
# x = 5
# y = x
# print(id(x) == id(y)) # if two variables have the same id() , you know they reference the same object
# ==================================================================================
# Lesson 8
# help("keywords") # returns
# """
#   False               class               from                or
#   None                continue            global              pass
#   True                def                 if                  raise
#   and                 del                 import              return
#   as                  elif                in                  try
#   assert              else                is                  while
#   async               except              lambda              with
#   await               finally             nonlocal            yield
#   break               for                 not
# """

# Lesson 9
# ----------------------------
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------

# Back Space
# print("Hello\bWorld")  # Will Remove o

# Escape New Line + Back Slash
# print("Hello \
# I Love \
# Python")

# Escape Back Slash
# print("I Love Back Slash \\")

# Escape Single Quote
# print('I Love Single Quote \'Test\' ')

# Escape Double Quotes
# print("I Love Double Quotes \"Test\" ")

# Line Feed
# print("Hello World\nSecond Line")

# Carriage Return
# print("123456\rAbcde")

# Horizontal Tab
# print("Hello\tPython")

# Character Hex Value
# print("\x4F\x73")
# ==================================================================================
# Lesson 10
# -- Concatenation --

# msg = "I Love"
# lang = "Python"
# print(msg + " " + lang)

# full = msg + " " + lang
# print(full)

# a = "First \
# Second \
# Third"

# b = "A \
# B \
# C"

# print(a + "\n" + b)

# print("Hello " + 1)  # Error
# ==================================================================================
# Ass 1
# name = "ahmed"
# age = 20
# country = "Egypt"
# print("\"Name: "+name+"\"\n"
#       "\"Age: " + str(age)+"\"\n"
#       "\"Country: "+country+"\"\n")
# print("\"Hello, My name is " + name +" and i am " + str(age) + "years old and i live in " + country)
# print(type(name))
# print(type(country))
# print(type(str(age)))


###Coding
# x = input() here x will hava data type string as it auto takes the input as string , if we want to take integer : int(input())
# in python there is no concatenation just str on int
# x = input() //5 this is str
# y = input() //3.0 this is str
# print(x + y) //53.5 # and this wrong to make it right we use int(input())
# (True , False , < , > , == , <= , >= ,!=) is comparison operations
# (and , or , != ) is logical operations
#  == can compare 2 strings
#
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
