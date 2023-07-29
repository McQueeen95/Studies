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
# Assignment 1
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
# ==================================================================================
# Lesson 11
# -------------
# -- Strings --
# -------------

# myStringThree = 'This is Single Quote "Test"'
# myStringFour = "This is Double Quotes 'Test'" #you can put "" or '' inside the other without using escape sequence

# print(myStringThree)
# print(myStringFour)

# myStringFive = '''First # you can use ''' text text ''' to write on mulitple lines
# Second 'Test' "Test"
# Third'''

# myStringSix = """First
# Second "Test" \\\ 'Test'
# Third"""

# print(myStringFive)
# print(myStringSix)
# ==================================================================================
# Lesson 12
# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

# myString = "I Love Python"

# print(myString[0])  # Index 0 => I
# print(myString[9])  # Index 9 => t

# print(myString[-1])  # Index -1 => First Character From End
# print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

# print(myString[8:11])  # yth
# print(myString[3:5])  # ov

# print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
# print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
# print(myString[:])  # Full Data

# print(myString[0::1])  # Full Data
# print(myString[::1])  # Full Data

# print(myString[::2]) # with 2 steps
# print(myString[::3]) # with 3 steps
# ==================================================================================
# Lesson 13
# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

# a = "    I Love Python    "
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
# a = "#####I Love Python####"
# print(a.strip("#"))
# print(a.rstrip("#"))
# print(a.lstrip("#"))
# a = "@#@#@#I Love Python@#@#@#"
# print(a.strip("@#")) # removes those elements from both sides
# print(a.rstrip("@#")) # removes those elements from right side
# print(a.lstrip("@#")) # removes those elements from left side

# # title()

# b = "I love 2d graphics and 3g Technology and python"
# print(b.title()) # every first letter and every litter after a number => capital

# # capitalize()

# b = "love 2d graphics and 3g Technology and python"
# print(b.capitalize()) # just the first letter in string => capital & rest letter => small

# # zfill (make the number being like a counter)

# c, d, e, f = "1", "11", "111", "1111"
# print(c.zfill(4))
# print(d.zfill(4))
# print(e.zfill(4))
# print(f.zfill(4))

# # upper()

# g = "osama"
# print(g.upper())

# # lower()

# h = "OSama"
# print(h.lower())
# ==================================================================================
# Lesson 14

# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

# a = "I Love Python and PHP and MySQL"
# print(a.split()) # returns a list contains every word in the string that splie by (space or any seprator)
# b = "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-"))
# c = "I-Love-Python-and-PHP-and-MySQL"
# print(c.split("-", 3)) # 2rd parameter is the number of objects that gonna seprate
# d = "I-Love-Python-and-PHP-and-MySQL"
# print(d.rsplit("-", 3)) # same but from the other side

# # center() #fill with signs at the right and left of the string

# e = "Osama"
# print(e.center(9))  # Spaces
# print(e.center(9, "#"))  # Hashes
# print(e.center(15, "@"))  # @

# # count() # returns The number of repetitions of a given string

# f = "I Love Python and PHP Because PHP is Easy"
# print(f.count("PHP"))  # 2 PHP Words
# print(f.count("PHP", 0, 25))  # Only One PHP Word

# # swapcase()

# g = "I Love Python"
# h = "i lOVE pYTHON"

# print(g.swapcase()) # capital => small and otherwise
# print(h.swapcase())

# # startswith()

# i = "I Love Python"
# print(i.startswith("I")) #return boolean value of the check
# print(i.startswith("S"))
# print(i.startswith("P", 7,)) # same but with specific indexes

# # endswith()

# j = "I Love Python"
# print(j.endswith("n"))
# print(j.endswith("S"))
# print(j.endswith("e", 2, 6))
# ==================================================================================
# Lesson 15

# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)

# a = "I Love Python"
# # print(a.index("P"))  # Index Number 7
# # print(a.index("P", 0, 10))  # Index Number 7
# # print(a.index("P", 0, 5))  # Through Error

# # find(SubString, Start, End)

# b = "I Love Python"
# print(b.find("P"))  # Index Number 7
# print(b.find("P", 0, 10))  # Index Number 7
# print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) #puts the string at right and fill the symbol at left
# ljust(Width, Fill Char) #puts the string at left and fill the symbol at right

# c = "Osama"
# print(c.rjust(10))
# print(c.rjust(10, "#"))
# print(c.ljust(10))
# print(c.ljust(10, "#"))

# # splitlines() returns a list contains each line as an element

# e = """First Line
# Second Line
# Third Line"""
# print(e.splitlines())
# f = "First Line\nSecond Line\nThird Line"
# print(f.splitlines())

# # expandtabs() \t => tap with specific space

# g = "Hello\tWorld\tI\tLove\tPython"
# print(g.expandtabs(5))

# var.istitle()

# one = "I Love Python And 3G"
# two = "I Love Python And 3g"
# print(one.istitle())
# print(two.istitle())

# var.isspace()

# three = " "
# four = ""
# print(three.isspace())
# print(four.isspace())

# five = 'i love python'
# six = 'I Love Python'
# print(five.islower())
# print(six.islower())

# seven = "osama_elzero"
# eight = "OsamaElzero100"
# nine = "Osama--Elzero100"

# print(seven.isidentifier())
# print(eight.isidentifier())
# print(nine.isidentifier())

# var.isalpha() returns a boolean value after checks if it a => z or A => Z

# x = "AaaaaBbbbbb"
# y = "AaaaaBbbbbb111"
# print(x.isalpha())
# print(y.isalpha())

# var.isalnum() returns a boolean value after checks if it a => z or A => Z or 0 => 9

# u = "AaaaaBbbbbb"
# z = "AaaaaBbbbbb111"
# print(u.isalnum())
# print(z.isalnum())

# ==================================================================================
# lesson 16

# ---------------------
# -- Strings Methods --
# ---------------------

# replace(Old Value, New Value, Count)

# a = "Hello One Two Three One One"
# print(a.replace("One", "1"))
# print(a.replace("One", "1", 1))
# print(a.replace("One", "1", 2))

# join(Iterable) returns a string from iterable(list , tuples , ...) and join them with specifec seperate operator

# myList = ["Osama", "Mohamed", "Elsayed"]
# print("-".join(myList))
# print(" ".join(myList)) ; print(*myList) # those prints the same string
# print(" and ".join(myList))
# print(", ".join(myList))
# print(type(", ".join(myList)))

# ==================================================================================
# lesson 17

# ------------------------
# -- Strings Formatting(old way using %) --
# ------------------------

# name = "Osama"
# age = 36
# rank = 10

# print("My Name is: %s" % name)
# print("My Name is: %s and My Age is: %d" % (name, age))
# print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %.5s => String with the first 5 letters
# %d => Digit(integer)
# %f => Float
# %.2f => Float with 2 digits after the dot (x.00)

# Control Floating Point Number

# myNumber = 10
# print("My Number is: %d" % myNumber)
# print("My Number is: %f" % myNumber)
# print("My Number is: %.2f" % myNumber)

# Truncate String

# myLongString = "Hello Peoples of Elzero Web School I Love You All"
# print("Message is %s" % myLongString)
# print("Message is %.5s" % myLongString)

# ==================================================================================
# Lesson 18

# ---------------------------------
# -- Strings Formatting (New Ways using {}) --
# ---------------------------------

# name = "Osama"
# age = 36
# rank = 10

# print("My Name is: {}".format(name))
# print("My Name is: {} My Age: {}".format(name, age))
# print("{:s} is my fav youtuber and hes age is {:d} and its rank is {:.2f}".format(name,age,rank))
# {:s} => String
# {:.5s} => String with the first 5 letters
# {:d} => Number
# {:f} => Float
# {:.2f} => Float with 2 digits after the dot (x.00)

# # Control Floating Point Number

# myNumber = 10
# print("My Number is: {:d}".format(myNumber))
# print("My Number is: {:f}".format(myNumber))
# print("My Number is: {:.2f}".format(myNumber))

# # Truncate String

# myLongString = "Hello Peoples of Elzero Web School I Love You All"
# print("Message is {}".format(myLongString))
# print("Message is {:.5s}".format(myLongString))

# # Format Money

# myMoney = 500162350198

# print("My Money in Bank Is: {:d}".format(myMoney))
# print("My Money in Bank Is: {:_d}".format(myMoney))
# print("My Money in Bank Is: {:,d}".format(myMoney)) # seperate every 3 numbers with ,

# # ReArrange Items

# a, b, c = "One", "Two", "Three"
# print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
# print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
# print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two
# print("Hello {0} {0} {0}".format(a,b,c))

# x, y, z = 10, 20, 30
# print("Hello {} {} {}".format(x, y, z))
# print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
# print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
# print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# # Format in Version 3.6+

# myName = "Osama"
# myAge = 36

# print("My Name is : {myName} and My Age is : {myAge}")
# print(f"My Name is : {myName} and My Age is : {myAge}") # by putting f before the string we can make it like javascript
# ==================================================================================
# this a full info about the formating (https://pyformat.info/)
# padding and aligning strings
# old
# print("%10s of any u want" % "test")  # 10 spaces behind 'test'
# print('%-10s of any u want'% "test" ) #10 spaces after 'test'
# new (more control)
# print("hello this is {:>10}".format("test"))  # 10 spaces behind 'test'
# print("hello this is {:10}".format("test"))#10 spaces after 'test'
# print("hello this is {:_<10}".format("test"))  # 10 spaces after 'test'
# print("hello this is {:^10}".format("test"))  # 10 spaces 5 before 5 after
# ==================================================================================
## Assignment 2
# 1,2
# name = "ahmed"
# age = 20
# county = "Egypt"
# print('''
#       \"Hello '{}', How You Doing \\
#       \"\"\" Your Age Is \"{}\"\" +
#       And Your Country Is: {}
#       '''.format(name,age,county))

# 3,4
# name = "Elzero"
# print('''
#       Second Letter is "{}"
#       Third Letter Is "{}"
#       Last Letter Is "{}"'''.format(name[1],name[2],name[-1]))
# print('''
#       "{}"
#       "{}"
#       "{}"'''.format(name[1:4],name[::2],name[-2::-2]))

# 5
# name = "#@#@Elzero#@#@"
# print(name.strip("#@"))

# 6
# num = "1500"
# print(num.zfill(4))

# 7
# name1 = "Ahmed"
# name2 ="Ahmed MOhamed"
# print(name1.rjust(20,"@"))
# print(name2.rjust(20,"@"))

# 8
# name1 = "OSamA"
# name2 = "osaMA"
# print(name1.swapcase())
# print(name2.swapcase())

# 9
# msg = "I Love Python And Although Love Elzero Web School"
# print(msg.count("Love"))

# 10
# name = "elzero"
# print(name.find("z"))

# 11
# msg = "I <3 Python And Although <3 Elzero Web School"
# print(msg.replace("<3","Love",1))

# 12
# msg = "I <3 Python And Although <3 Elzero Web School"
# print(msg.replace("<3","Love"))

# 13
# name = "Osama"
# age = 38
# country = "Egypt"
# print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
# ==================================================================================
# Lesson 19
# -------------
# -- Numbers --
# -------------
# Integer
# print(type(1))
# print(type(100))
# print(type(10))
# print(type(-10))
# print(type(-110))
# Float
# print(type(1.500))
# print(type(100.99))
# print(type(-10.99))
# print(type(0.99))
# print(type(-0.99))
# Complex
# myComplexNumber = 5+6j
# print(type(myComplexNumber))
# print("Real Part Is: {}".format(myComplexNumber.real))
# print("Imaginary Part Is: {}".format(myComplexNumber.imag))
# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type
# print(100)
# print(float(100))
# print(complex(100))
# print(10.50)
# print(int(10.50))
# print(complex(10.50))
# print(10+9j)
# print(int(10+9j))
# ==================================================================================
# Lesson 20
# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------
# Addition
# print(10 + 30)  # 40
# print(-10 + 20)  # 10
# print(1 + 2.66)  # 3.66
# print(1.2 + 1.2)  # 2.4
# # Subtraction
# print(60 - 30)  # 30
# print(-30 - 20)  # -50
# print(-30 - -20)  # -10
# print(5.66 - 3.44)  # 2.22
# # Multiplication
# print(10 * 3)  # 30
# print(5 + 10 * 100)  # 1005
# print((5 + 10) * 100)  # 1500
# # Division
# print(100 / 20)  # 5.0
# print(int(100 / 20))  # 5
# # Modulus
# print(8 % 2)  # 0
# print(9 % 2)  # 1
# print(20 % 5)  # 0
# print(22 % 5)  # 2
# # Exponent
# print(2 ** 5)  # 32
# print(2 * 2 * 2 * 2 * 2)  # 32
# print(5 ** 4)  # 625
# print(5 * 5 * 5 * 5)  # 625
# # Floor Division
# print(100 // 20)  # 5
# print(119 // 20)  # 5
# print(120 // 20)  # 6
# print(140 // 20)  # 7
# print(142 // 20)  # 7
# ==================================================================================
## Assignment 3
# 1
# print(type(1))
# print(type(1.0))
# print(type(1+2j))

# 2
# x = 1 + 2j
# print(x.real)
# print(x.imag)

# 3
# x = 10
# print("{:.10f}".format(x))

# 4
# x = 159.650
# print(int(x))
# print(type(int(x)))
# ==================================================================================
# Lesson 21
# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------
# myAwesomeList = ["One", "Two", "One", 1, 100.5, True]
# print(myAwesomeList)  # Whole List
# print(myAwesomeList[1])  # "Two"
# print(myAwesomeList[-1])  # True
# print(myAwesomeList[-3])  # 1
# print(myAwesomeList[1:4])  # ['Two', 'One', 1]
# print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
# print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]
# print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
# print(myAwesomeList[::2])  # ['One', 'One', 100.5]
# print(myAwesomeList) # ['One', 'Two', 'One', 1, 100.5, True]
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
# myAwesomeList[0:3] = ["A"]
# print(myAwesomeList)
# ==================================================================================
# Lesson 22
# -------------------
# -- Lists Methods --
# -------------------
# # append()
# myFriends = ["Osama", "Ahmed", "Sayed"]
# myOldFriends = ["Haytham", "Samah", "Ali"]
# myFriends.append("Alaa")
# myFriends.append(100)
# myFriends.append(150.200)
# myFriends.append(True)
# myFriends.append(myOldFriends)
# print(myFriends)
# print(myFriends[2])
# print(myFriends[6])
# print(myFriends[7])
# print(myFriends[7][2])
# # extend()
# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# c = ["One", "Two"]
# a.extend(b)
# a.extend(c)
# print(a)
# # remove()
# x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
# x.remove("Osama")
# print(x)
# # sort()
# y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"] 
# y.sort(reverse=True)
# y.sort()
# print(y)
# # reverse()
# z = [10, 1, 9, 80, 100, "Osama", 100]
# z.reverse()
# print(z)
# ==================================================================================
# Lesson 23
# -------------------
# -- Lists Methods --
# -------------------
# # clear()
# a = [1, 2, 3, 4]
# a.clear()
# print(a)
# # copy()
# b = [1, 2, 3, 4]
# c = b.copy()
# print(b)  # Main List
# print(c)  # Copied List
# b.append(5)
# print(b)  # Main List
# print(c)  # Copied List
# # count()
# d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
# print(d.count(1))
# # index()
# e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
# print(e.index("Ramy"))
# # insert()
# f = [1, 2, 3, 4, 5, "A", "B"]
# f.insert(0, "Test")
# f.insert(-1, "Test") # it insert the new element before the given index
# f.insert(len(f),"final")
# print(f)
# # pop()
# g = [1, 2, 3, 4, 5, "A", "B"]
# print(g.pop(-3))
# ==================================================================================
# Assignment 4
# 1,2,3,4,5,6,8,9
# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# print(friends[0])
# print(friends[-5])
# print(friends[-1])
# print(friends[4])
# print(friends[0::2])
# print(friends[1::2])
# print(friends[1:4])
# print(friends[3:])
# friends[3:5] = ["Elzero","Elzero"]
# friends.insert(0,"mona")
# friends.insert(len(friends),"yousef")
# friends.remove(friends[0])
# friends.remove(friends[0])
# print(friends)
# friends.remove(friends[-1])
# print(friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# print(len(friends))

# 7
# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# friends.extend(employees)
# friends.extend(school)
# print(friends)

# 10
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# print(technologies[-1][0])
# print(technologies[-1][-1])
# ==================================================================================
# Lesson 24
# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------
# # Tuple Syntax & Type Test
# myAwesomeTupleOne = ("Osama", "Ahmed")
# myAwesomeTupleTwo = "Osama", "Ahmed"
# print(myAwesomeTupleOne)
# print(myAwesomeTupleTwo)
# print(type(myAwesomeTupleOne))
# print(type(myAwesomeTupleTwo))
# # Tuple Indexing
# myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
# print(myAwesomeTupleFive[1])
# print(myAwesomeTupleFive[-1])
# # Tuple Assign Values
# myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment
# ==================================================================================
# Lesson 25
# -----------
# -- Tuple --
# -----------
# # Tuple With One Element
# myTuple1 = ("Osama",) # we put commas to be a tuble , if we don't it become string
# myTuple2 = "Osama",
# print(myTuple1)
# print(myTuple2)
# print(type(myTuple1))
# print(type(myTuple2))
# print(len(myTuple1))
# print(len(myTuple2))
# # Tuple Concatenation
# a = (1, 2, 3, 4)
# b = (5, 6)
# c = a + b
# d = a + ("A", "B", True) + b
# print(c)
# print(d)
# # Tuple, List, String Repeat (*)
# myString = "Osama"
# myList = [1, 2]
# myTuple = ("A", "B")
# print(myString * 6)
# print(myList * 6)
# print(myTuple * 6)
# # Methods => count()
# a = (1, 3, 7, 8, 2, 6, 5, 8)
# print(a.count(8))
# # Methods => index()
# b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: {:d}".format(b.index(7)))
# print(f"The Position of Index Is: {b.index(7)}") # another way to write it
# # Tuple Destruct
# a = ("A", "B", 4, "C") # 3 var for tuble of len 3 , anything else is error
# x, y, _, z = a # we can make _ var to take valuse we don't need
# print(_)
# print(x)
# print(y)
# print(z)
# ==================================================================================
# Assignment 5
# 1
# x = "Ahmed",
# print(f"\"{x[0]}\" and this is {type(x)}")

# 2
# friends = ("Osama", "Ahmed", "Sayed")
# lsf = list(friends)
# lsf[0] = "Elzero"
# print(f"{tuple(lsf)} and this is {type(friends)} and the len is{len(friends)}")

# 3
# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# x = nums+letters
# print(f"nums_and_letters_one = {x}")
# print(f"{len(x)} Elements")

# 4
# my_tuple = (1, 2, 3, 4)
# a ,b,_,c = my_tuple
# print(a)
# print(b)
# print(c)
#