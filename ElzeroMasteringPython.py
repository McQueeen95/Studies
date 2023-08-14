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
# ==================================================================================
# Lesson 26
# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------
# Not Ordered And Not Indexed
# every run go with diffrent order
# mySetOne = {"Osama", "Ahmed", 100}
# print(mySetOne)
# print(mySetOne[0]) # error
# Slicing Cant Be Done
# mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3]) #error
# Has Only Immutable Data Types # any i can modifiy is not accepted
# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
# mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}
# print(mySetThree)
# Items Is Unique # any repeated object is gone
# mySetFour = {1, 2, "Osama", "One", "Osama", 1}
# print(mySetFour)
# ==================================================================================
# Lesson 27
# -----------------
# -- Set Methods --
# -----------------
# # clear()
# a = {1, 2, 3}
# a.clear()
# print(a)
# # union()
# b = {"One", "Two", "Three"}
# c = {"1", "2", "3"}
# x = {"Zero", "Cool"}
# print(b | c)
# print(b.union(c, x))
# # add()
# d = {1, 2, 3, 4}
# d.add(5)
# d.add(6)
# print(d)
# # copy()
# e = {1, 2, 3, 4}
# f = e.copy()
# print(e)
# print(f)
# e.add(6)
# print(e)
# print(f)
# # remove()
# g = {1, 2, 3, 4}
# g.remove(1)
# g.remove(7) # if some element is DNE it returns an error
# print(g)
# # discard()
# h = {1, 2, 3, 4}
# h.discard(1)
# h.discard(7) # if some element is Exist it doesn't return an error
# print(h)
# # pop()
# i = {10,(0,2),"hi",'H',4.44}
# print(i.pop()) # returns a random element from the set
# # update()
# j = {1, 2, 3}
# k = {1, "A", "B", 2}
# j.update(['Html', "Css"])
# j.update(k)
# print(j)
# ==================================================================================
# Lesson 28
# -----------------
# -- Set Methods --
# -----------------
# # difference() # elements that exists in first and not in second (difference)
# a = {1, 2, 3, 4}
# b = {1, 2, 3, "Osama", "Ahmed"}
# print(a)
# print(a.difference(b))  # a - b
# print(a)
# # difference_update()
# c = {1, 2, 3, 4}
# d = {1, 2, "Osama", "Ahmed"}
# print(c)
# c.difference_update(d)  # c - d
# print(c) # here its update the c with the result of the operation
# # intersection()
# e = {1, 2, 3, 4, "X", "Osama"}
# f = {"Osama", "X", 2}
# print(e)
# print(e.intersection(f))  # e & f
# print(e)
# # intersection_update()
# g = {1, 2, 3, 4, "X", "Osama"}
# h = {"Osama", "X", 2}
# print(g)
# g.intersection_update(h)  # g & h
# print(g)
# # symmetric_difference()
# i = {1, 2, 3, 4, 5, "X"}
# j = {"Osama", "Zero", 1, 2, 4, "X"}
# print(i)
# print(i.symmetric_difference(j))  # i ^ j
# print(i)
# # symmetric_difference_update()
# k = {1, 2, 3, 4, 5, "X"}
# l = {"Osama", "Zero", 1, 2, 4, "X"}
# print(k)
# k.symmetric_difference_update(l)  # k ^ l
# print(k)
# ==================================================================================
# Lesson 29
# -----------------
# -- Set Methods --
# -----------------
# # issuperset() # returns true if all elements in 2nd set is inside the 1st set
# first = {1, 2, 3, 4}
# second = {1, 2, 3}
# c = {1, 2, 3, 4, 5}
# print(first.issuperset(second))  # True
# print(first.issuperset(c))  # False
# # issubset() # returns true if all alements in 1st set is inside the 2nd set
# d = {1, 2, 3, 4}
# e = {1, 2, 3}
# f = {1, 2, 3, 4, 5}
# print(d.issubset(e))  # False
# print(d.issubset(f))  # True
# # isdisjoint() # return false if there is mutual elemets between the two sets
# g = {1, 2, 3, 4}
# h = {1, 2, 3}
# i = {10, 11, 12}
# print(g.isdisjoint(h))  # False
# print(g.isdisjoint(i))  # True
# ==================================================================================
# Lesson 30
# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------
# user = {
#   "name": "Osama",
#   "age": 36,
#   "country": "Egypt",
#   "skills": ["Html", "Css", "JS"],
#   "rating": 10.5
# }
# print(user)
# print(user['country'])
# print(user.get("country"))
# # Two-Dimensional Dictionary
# languages = {
#   "One": {
#     "name": "Html",
#     "progress": "80%"
#   },
#   "Two": {
#     "name": "Css",
#     "progress": "90%"
#   },
#   "Three": {
#     "name": "Js",
#     "progress": "90%"
#   }
# }
# print(languages)
# print(languages['One'])
# print(languages['Three']['name'])
# # Dictionary Length
# print(len(languages))
# print(len(languages["Two"]))
# # Create Dictionary From Variables
# frameworkOne = {
#   "name": "Vuejs",
#   "progress": "80%"
# }
# frameworkTwo = {
#   "name": "ReactJs",
#   "progress": "80%"
# }
# frameworkThree = {
#   "name": "Angular",
#   "progress": "80%"
# }
# allFramework = {
#   "one": frameworkOne,
#   "two": frameworkTwo,
#   "three": frameworkThree
# }
# print(allFramework)
# ==================================================================================
# Lesson 31
# ------------------------
# -- Dictionary Methods --
# ------------------------
# # clear()
# user = {
#   "name": "Osama"
# }
# print(user)
# user.clear()
# print(user)
# # update()
# member = {
#   "name": "Osama"
# }
# print(member)
# member["age"] = 36 # we can add a new key:value manually like this
# print(member)
# member.update({"country": "Egypt"}) # or add it by the update() method
# print(member)
# # copy()
# main = {
#   "name": "Osama"
# }
# b = main.copy()
# print(b)
# main.update({"skills": "Fighting"})
# print(main)
# print(b)
# # keys() + values()
# print(main.keys())
# print(main.values())
# ==================================================================================
# Lesson 32
# ------------------------
# -- Dictionary Methods --
# ------------------------
# setdefault()
# user = {
#   "name": "Osama"
# }
# print(user)
# print(user.setdefault("age", 36)) # if there isn't "age" key , it add it with its value 36 and return it (value)
# print(user.setdefault("name", "Ahmed")) # if there is the "name" key it returns its value , if not its add it with "name": Ahmed
# print(user)
# # popitem()
# member = {
#   "name": "Osama",
#   "skill": "PS4"
# }
# print(member)
# member.update({"age": 36})
# print(member.popitem()) # returns the last item added to the dictionary
# # items()
# view = {
#   "name": "Osama",
#   "skill": "XBox"
# }
# print(view.items()) # items of view in a list and every element is in a tuple
# print(view)
# print(view.items())
# view["age"] = 36 # adds new item
# print(view.items())
# # fromkeys()
# a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree') # tuple
# b = "X"
# c = ["hi one","hi two","hi three"]
# print(dict.fromkeys(a, b)) # making a dictionary from keys and one value
# print(dict.fromkeys(a,c)) # every key take the same value
# ==================================================================================
# Assignment 6
# 1 (in more advance)
# x = [1,5,4,3,3,2,1]
# uqX = set(x)
# print(*uqX) # to print with unpack it to be without , and {}
# print(" ".join(uqX))  # same but with useing join
# print(enumerate(uqX)) # return an enumerate object
# for i,element in enumerate(uqX): # assigns the index of the current element to the variable i and the value of the current element to the variable element.
#   if i == len(uqX)-1: # this to print it with , but not with {}
#     print(element)
#   else:
#     print(element,end=",")

# 1
# my_list = [1, 2, 3, 3, 4, 5, 1]
# unique_list = list(set(my_list))
# print(",".join([str(x) for x in unique_list]))
# print(type(unique_list))
# print(",".join([str(x) for x in unique_list[:-1]]))

# 2
# nums = {1,2,3}
# letters = {'A','B','C'}
# print(nums | letters)
# print(nums.union(letters))
# nums.update(letters)
# print(nums)

# 3
# my_set = {1, 2, 3}
# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update(["A","B"])
# print(my_set)
# my_set.discard("C")

# 4
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}
# print(set_one.issubset(set_two))

# 5
# exp = {
#   "first":{
#     "name" : "HTML",
#     "progress" : "90%"
#   },
#   "second":{
#     "name" : "CSS",
#     "progress" : "80%"
#   },
#   "Third":{
#     "name" : "Python",
#     "progress" : "40%"
#   }
# }
# print(f'"{exp["first"]["name"]} Progress is {exp["first"]["progress"]}"')
# print(f'"{exp["second"]["name"]} Progress is {exp["second"]["progress"]}"')
# print(f'"{exp["Third"]["name"]} Progress is {exp["Third"]["progress"]}"')
# exp["fourth"] = {
#     "name" : "AI",
#     "progress" : "20%"
# }
# print(f'"{exp["fourth"]["name"]} Progress is {exp["fourth"]["progress"]}"')
# ==================================================================================
# Lesson 33
# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------
# name = " "
# print(name.isspace())
# # True Values
# print(bool("Osama"))
# print(bool(100))
# print(bool(100.95))
# print(bool(True))
# print(bool([1, 2, 3, 4, 5]))
# # False Values
# print(bool(0))
# print(bool(""))
# print(bool(''))
# print(bool([]))
# print(bool(False))
# print(bool(()))
# print(bool({}))
# print(bool(None))
# ==================================================================================
# Lesson 34
# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------
# age = 36
# country = "Egypt"
# rank = 10
# print(age > 16 and country == "Egypt" and rank > 0)  # True
# print(age > 16 and country == "KSA" and rank > 0)  # False
# print(age > 40 or country == "KSA" or rank > 20)  # False
# print(age > 40 or country == "Egypt" or rank > 20)  # True
# print(age > 16)  # True
# print(not age > 16)  # Not True = False
# print(not((True and True) and (False or True)))
# ==================================================================================
# Lesson 35
# --------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------
# x = 10  # Var One
# y = 20  # Var Two
# Var One = Self [Operator] Var Two
# Var One [Operator]= Var Two
# x += y
# x -= y
# print(x)
# ==================================================================================
# Lesson 36
# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------
# # Equal + Not Equal
# print(100 == 100)
# print(100 == 100.00)
# print(100 != 100)
# print(100 != 100.00)
# # Greater Than + Less Than
# print(100 > 100.00)
# print(100 > 40)
# print(100 < 100.00)
# print(100 < 40)
# # Greater Than Or Equal + Less Than Or Equal
# print(100 >= 100.00)
# print(100 <= 100.00)
# ==================================================================================
# Lesson 37
# ---------------------
# -- Type Conversion --
# ----------------------
# # int()
# st = "345"
# print(int(st))
# # str()
# a = 10
# print(type(a))
# print(type(str(a)))
# # tuple()
# c = "Osama"  # String
# d = [1, 2, 3, 4, 5]  # List
# e = {"A", "B", "C"}  # Set (unorderd)
# f = {"A": 1, "B": 2}  # Dictionary
# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))
# # list()
# c = "Osama"  # String
# d = (1, 2, 3, 4, 5)  # Tuple
# e = {"A", "B", "C"}  # Set
# f = {"A": 1, "B": 2}  # Dictionary
# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))
# # set() (all gonna be unordered)
# c = "Osama"  # String
# d = (1, 2, 3, 4, 5)  # Tuple
# e = ["A", "B", "C"]  # List
# f = {"A": 1, "B": 2}  # Dictionary
# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))
# # dict()
# d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
# e = [["One", 1], ["Two", 2], ["Three", 3]]  # List
# print(dict(d))
# print(dict(e))
# ==================================================================================
# Assignment 7
# 1
# print(bool(True))
# print(bool([1,2]))
# print(bool("hi"))
# print(bool({1,2}))
# print(bool(False))
# print(bool(""))
# print(bool([]))
# print(bool({}))

# 2
# html = 80
# css = 60
# javascript = 70
# print(html > 50 and css > 50 and javascript > 50)

# 3
# num_one = 10
# num_two = 20
# num = 20
# print(num > num_one or num > num_two)
# print(num > num_one and num > num_two)

# 4
# num_one = 10
# num_two = 20
# result = num_two + num_one
# print(result)
# print(result**3)
# print((result**3) % 2600)
# print(((result**3) % 2600) / 5)
# print(type(str(((result**3) % 2600) / 5)))
# ==================================================================================
# Lesson 38
# ----------------
# -- User Input --
# ----------------
# fName = input('What\'s Is Your First Name?')
# mName = input('What\'s Is Your Middle Name?')
# lName = input('What\'s Is Your Last Name?')
# fName = fName.strip().capitalize()
# mName = mName.strip().capitalize()
# lName = lName.strip().capitalize()
# print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")
# ==================================================================================
# Lesson 39
# ---------------------------
# -- Practical Slice Email --
# ---------------------------
# theName = input('What\'s Your Name ?').strip().capitalize()
# theEmail = input('What\'s Your Email ?').strip()
# theUsername = theEmail[:theEmail.index("@")]
# theWebsite = theEmail[theEmail.index("@") + 1:]
# print(f"Hello {theName} Your Email Is {theEmail}")
# print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")
# ==================================================================================
# Lesson 40
# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------
# age = int(input('What\'s Your Age ? ').strip())
# months = age * 12
# weeks = months * 4
# days = weeks * 7
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print('You Lived For:')
# print(f"{months} Months.")
# print(f"{weeks:,} Weeks.")
# print(f"{days:,} Days.")
# print(f"{hours:,} Hours.")
# print(f"{minutes:,} Minutes.")
# print(f"{seconds:,} Seconds.")
# ==================================================================================
# Assignment 8
# 1
# name = input("ur name is: ").strip().capitalize()
# print(f"Hello {name}, we missed u bro.. I missed u , all I want in this life is your eyes infrontof me every sec")

# 2
# age = int(input("ur age is:"))
# if age < 16:
#   print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#   print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

# 3
# firstName = input("ur first name is:").strip().capitalize()
# lastName = input("ur last name is:").strip().capitalize()
# print(f"Hello {firstName} {lastName:.1s}")

# 4
# email = input("ur email is:").strip().lower()
# print(email[:email.index("@")].capitalize())
# print(email[email.index("@")+1:email.index(".")])
# print(email[email.index(".")+1:])
# ==================================================================================
# Lesson 41, 42
# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# -- Nested If -------
# --------------------
# uName = "Osama"
# isStudent = "Yes"
# uCountry = "Egypt"
# cName = "Python Course"
# cPrice = 100
# if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":
#   if isStudent == "Yes":
#     print(f"Hi {uName} Because U R From {uCountry} And Student")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")
#   else:
#     print(f"Hi {uName} Because U R From {uCountry}")
#     print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")
# elif uCountry == "Kuwait" or uCountry == "Bahrain":
#   print(f"Hi {uName} Because U R From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")
# else:
#   print(f"Hi {uName} Because U R From {uCountry}")
#   print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")
# ==================================================================================
# Lesson 43
# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------
# country = "A"
# if country == "Egypt" : print(f"The Weather in {country} Is 15")
# elif country == "KSA" : print(f"The Weather in {country} Is 30")
# else : print("Country is Not in The List")
# # Short If
# movieRate = 18
# age = 18
# print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")
# # Condition If True | If Condition | Else | Condition If False
# print(True if int(input()) > 8 else False)
# ==================================================================================
# Lesson 44
# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------
# print("#" * 80)
# print(" You Can Write any Letter Or Full Name of The Time Unit ".center(80, "#"))
# print(" And i gonna give u how much u lived ".center(80, "#"))
# print("#" * 80)
# age = int(input("ur age:"))
# choise = (input("now choose between month,day,week or any letter of them: ").strip().lower())
# months = age * 12
# weeks = months * 4
# days = age * 365
# lm = ["m", "o", "t", "h", "n"]
# lw = ["w", "e", "k"]
# ld = ["d", "a", "y"]

# if choise == "month" or choise in lm:
#     print("You Choosed The Unit Months")
#     print(f"You Lived For {months:,} Months.")
# elif choise == "weeks" or choise in lw:
#     print("You Choosed The Unit Weeks")
#     print(f"You Lived For {weeks:,} Weeks.")
# elif choise == "days" or choise in ld:
#     print("You Choosed The Unit Days")
#     print(f"You Lived For {days:,} Days.")
# ==================================================================================
# Lesson 45
# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------
# # String
# name = "Osama"
# print("s" in name)
# print("a" in name)
# print("A" in name)
# # List
# friends = ["Ahmed", "Sayed", "Mahmoud"]
# print("Osama" in friends)
# print("Sayed" in friends)
# print("Mahmoud" not in friends)
# # Using In and Not In With Condition
# countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
# countriesOneDiscount = 80
# countriesTwo = ["Italy", "USA"]
# countriesTwoDiscount = 50
# myCountry = "Italy"
# if myCountry in countriesOne:
#   print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")
# elif myCountry in countriesTwo:
#   print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")
# else:
#   print("You Have No Discount")
# ==================================================================================
# Lesson 46
# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------
# # List Contains Admins
# admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]
# # Login
# name = input("Please Type Your Name ").strip().capitalize()
# # If Name is In Admin
# if name in admins:
#   print(f"Hello {name} Welcome Back")
#   option = input("Delete Or Update Your Name ?").strip().capitalize()
#   # Update Option
#   if option == 'Update' or option == 'U':
#     theNewName = input("Your New Name Please ").strip().capitalize()
#     admins[admins.index(name)] = theNewName
#     print("Name Updated.")
#     print(admins)
#   # Delete Option
#   elif option == 'Delete' or option == 'D':
#     admins.remove(name)
#     print("Name Deleted")
#     print(admins)
#   # Wrong Option
#   else:
#     print("Wrong Option Choosed")
# else:
#   status = input("Not Admin, Add You Y, N ? ").strip().capitalize()
#   if status == "Yes" or status == "Y":
#     print("You Have Been Added")
#     admins.append(name)
#     print(admins)
#   else:
#     print("You Are Not Added.")
# ==================================================================================
# Assignment 9
# 1
# while True:
#   num1 = int(input("first num: "))
#   num2 = int(input("second number: "))
#   operation = input("Select opr (+ , - , * , / , %) or E to Exit ").strip().lower()
#   if operation == 'e':
#     print(f"Exiting the program..")
#     break
#   elif operation in ['+', '-', '*', '/', '%']:
#     if operation == '+':
#       result = num1+num2
#     elif operation == '-':
#       result = num1-num2
#     elif operation == '*':
#       result = num1*num2
#     elif operation == '/':
#       result = num1/num2
#     elif operation == '%':
#       result = num1%num2
#     print(f"Result: {num1} {operation} {num2} = {result}")
#   else :
#     print("wrong choice bro ,select again")

# 2
# age = int(input())
# print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")

# 3
# age = int(input())
# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# if age > 100 or age < 10:
#   print("out of range")
# else:
#   print(f"Your Age In months Is {months:,} months")
#   print(f"Your Age In weeks Is {weeks:,} weeks")
#   print(f"Your Age In days Is {days:,} days")
#   print(f"Your Age In hours Is {hours:,} hours")
#   print(f"Your Age In minutes Is {minutes:,} minutes")
#   print(f"Your Age In seconds Is {seconds:,} seconds")

# 4
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# discount = 30
# price = 100
# country = input("ur country: ").strip().capitalize()
# if country in countries:
#   print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
# else:
#   print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
# ==================================================================================
# Lesson 47
# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------
# a = 0
# while a < 15:
#   print(a)
#   a += 1  # a = a + 1
# print("Loop is Done")  # True Become False
# while False:
#   print("Will Not Print")
# ==================================================================================
# Lesson 48
# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------
# myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]
# print(len(myF))  # List Length [10]
# a = 0
# while a < len(myF):  # a < 10
#   print(f"#{str(a + 1).zfill(3)} {myF[a]}")
#   a += 1  # a = a + 1
# else: # I gonna explain it after this lesson
#   print("All Friends Printed To Screen.")
# ==================================================================================
# Lesson 49
# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------
# # Empty List To Fill Later
# myFavouriteWebs = []
# # Maximum Allowed Websites
# maximumWebs = 5
# while maximumWebs > 0:
#   # Input The New Website
#   web = input("Website Name Without https:// ")
#   # Add The New Website To The List
#   myFavouriteWebs.append(f"https://{web.strip().lower()}")
#   # Decrease One Number From Allowed Websites
#   maximumWebs -= 1  # maximumWebs = maximumWebs - 1
#   # Print The Add Message
#   print(f"Website Added, {maximumWebs} Places Left")
#   # Print The List
#   print(myFavouriteWebs)
# else:
#   print("Bookmark Is Full, You Cant Add More")
# ==================================================================================
# Lesson 50
# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------
# tries = 3
# mainPassword = "000"
# inputPassword = input("Write Your Password: ")
# while inputPassword != mainPassword:  # True
#   tries -= 1  # tries = tries - 1
#   if tries == 0:
#     print("All Tries Is Finished.")
#     break
#   print(f"Wrong Password, { 'Last' if tries == 1 else tries } Chance Left")
#   inputPassword = input("Write Your Password: ")
# else:
#   print("Correct Password") # this just happens when the condition is false but when its true and the loop finishes its never show up
# print("now go out")
# ==================================================================================
# Assignment 10
# 1
# num = int(input("enter a number > 0: "))
# printed = 0
# if num <= 0:
#   print("its <= 0")
# else:
#   while num > 0:
#     if num-1 == 6 or num-1 == 0:
#       num -= 1
#       continue
#     else:
#       print(num-1)
#       printed +=1
#       num -= 1
# print(f"{printed} Numbers Printed Successfully.")

# 2
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif","sorry","ignored","Bigdata"]
# i = 0
# ignored = 0
# while i < len(friends):
#   if friends[i][0].upper() == friends[i][0]:
#     print(friends[i])
#     i += 1
#   else:
#     ignored += 1
#     i += 1
# print(f"Friends Printed And Ignored Names Count Is {ignored}")

# 3
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
# while skills:
#   print(f'"{skills.pop(0)}"')

# 4
# my_friends = ["hi","bro","good","very"]
# lenOfList = 4
# while lenOfList > 0 and lenOfList != 4:
#   name = input("Enter ur friend name: ").strip()
#   if name == name.upper():
#     print("Invalid Name")
#   elif name == name.lower():
#     my_friends.append(name.capitalize())
#     lenOfList -= 1
#     print(f"Friend {name} Added => 1st Letter Become Capital")
#     print(f"Names Left in List Is {lenOfList}")
#   elif name == name.capitalize():
#     my_friends.append(name)
#     lenOfList -= 1
#     print(f"Friend {name} Added")
#     print(f"Names Left in List Is {lenOfList}")
#   else:
#     print("Enter ur name like humans bro")
# else:
#   print("sorry the list is full")
# print(f"ur list is {my_friends}")
# ==================================================================================
# Lesson 51
# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------
# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in myNumbers:
#   print(number * 17)
#   if number % 2 == 0:  # Even
#     print(f"The Number {number} Is Even.")
#   else:
#     print(f"The Number {number} Is Odd.")
# else:
#   print("The Loop Is Finished") # not like else in while loop
# myName = "Osama"
# for letter in myName:
#   print(f" [ {letter.upper()} ] ")
# ==================================================================================
# Lesson 52
# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------
# # Range
# for number in range(1, 101):
#   print(number)
# # Dictionary
# mySkills = {
#   "Html": "90%",
#   "Css": "60%",
#   "PHP": "70%",
#   "JS": "80%",
#   "Python": "90%",
#   "MySQL": "60%"
# }
# print(mySkills['JS'])
# print(mySkills.get("Python"))
# for skill in mySkills:
#   print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}")
# ==================================================================================
# Lesson 53
# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------
# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]
# skills = ["Html", "Css", "Js"]
# for name in peoples:  # Outer Loop
#   print(f"{name} Skills Is: ")
#   for skill in skills:  # Inner Loop
#     print(f"- {skill}")
# Dictionary
# peoples = {
#   "Osama": {"Html": "70%", "Css": "80%", "Js": "70%"},
#   "Ahmed": {"Html": "90%", "Css": "80%", "Js": "90%"},
#   "Sayed": {"Html": "70%", "Css": "60%", "Js": "90%"},
# }
# for name in peoples:
#   print(f"Skills and Progress For {name} Is: ")
#   for skill in peoples[name]:
#     print(f"{skill} => {peoples[name][skill]}")
# ==================================================================================
# Lesson 54
# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------
# myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]
# # Continue
# for number in myNumbers:
#   if number == 13:
#     continue # skips the current iteration
#   print(number)
# # Break
# for number in myNumbers:
#   if number == 13:
#     break # break and exit from the loop
#   print(number)
# # Pass
# for number in myNumbers:
#   if number == 13:
#     pass # ignores this block of code
#   print(number)
# ==================================================================================
# Lesson 55
# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------
# mySkills = {
#   "HTML": "80%",
#   "CSS": "90%",
#   "JS": "70%",
#   "PHP": "80%"
# }
# print(mySkills.items()) # this returns the keys and values of each one
# for skill in mySkills:
#   print(f"{skill} => {mySkills[skill]}")
# for skill_key, skill_progress in mySkills.items():
#   print(f"{skill_key} => {skill_progress}")
# myUltimateSkills = {
#   "HTML": {
#     "Main": "80%",
#     "Pugjs": "80%"
#   },
#   "CSS": {
#     "Main": "90%",
#     "Sass": "70%"
#   }
# }
# for main_key, main_value in myUltimateSkills.items():
#   print(f"{main_key} Progress Is: ")
#   for child_key, child_value in main_value.items():
#     print(f"- {child_key} => {child_value}")
# ==================================================================================
# Assignment 11
# 1
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# order = 1
# for i in range(len(my_nums)):
#   if my_nums[i] % 5 == 0:
#     print(f"{order} => {my_nums[i]}")
#     order += 1
# else:
#   print("All numbers printed")

# 2
# for i in range(1,21):
#   if i == 6 or i == 8 or i == 12:
#     continue
#   print(str(i).zfill(2))
# else:
#   print("All numbers printed")

# 3
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# points = {
#   'A' : 100,
#   'B': 80,
#   'C' : 40
# }
# total = 0
# for key,value in my_ranks.items():
#   print(f"My rank in {key} is {value} and this Equal {points[value]}")
#   total += points[value]
# else:
#   print(f"Total points is {total}")

# 4
# students = {
#   "Ahmed": {
#     "Math": "A",
#     "Science": "D",
#     "Draw": "B",
#     "Sports": "C",
#     "Thinking": "A"
#   },
#   "Sayed": {
#     "Math": "B",
#     "Science": "B",
#     "Draw": "B",
#     "Sports": "D",
#     "Thinking": "A"
#   },
#   "Mahmoud": {
#     "Math": "D",
#     "Science": "A",
#     "Draw": "A",
#     "Sports": "B",
#     "Thinking": "B"
#   }
# }
# points = {
#   'A' : 100,
#   'B': 80,
#   'C' : 40,
#   'D' : 20
# }
# print(students['Ahmed']['Math'])
# print(points[students['Ahmed']['Math']]) # for understand how we gonna use the loop
# part 1 (without .items())
# for name in students:
#   total = 0
#   print('"------------------------------"')
#   print(f'"- Student Name => {name}"')
#   print('"------------------------------"')
#   for subject in students[name]:
#     print(f'"- {subject} => {points[students[name][subject]]} Points"')
#     total += points[students[name][subject]]
#   print(f'"Total Points For {name} is {total}')
# part 2 (with .items())
# for topKey,topValue in students.items():
#   total = 0
#   print('"------------------------------"')
#   print(f'"- Student Name => {topKey}"')
#   print('"------------------------------"')
#   for bottomKey,bottomValue in topValue.items():
#     print(f'"- {bottomKey} => {points[bottomValue]} Points"')
#     total += points[bottomValue]
#   print(f'"Total Points For {topKey} is {total}')
# ==================================================================================
# Lesson 56
# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY (Don't Repeat Yourself)
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ----------------------------------------
# def function_name():
#   return "Hello Python From Inside Function"
# dataFromFunction = function_name()
# print(dataFromFunction)
# ==================================================================================
# Lesson 57
# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------
# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument
# def say_hello(name):
#   print(f"Hello {name}")
# say_hello("Ahmed")
# def addition(n1, n2):
#   if type(n1) != int or type(n2) != int:
#     print("Only Integers Allowed")
#   else:
#     print(n1 + n2)
# addition(100, 500)
# def full_name(first, middle, last):
#   print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")
# full_name("   osama   ", 'mohamed', "elsayed")
# ==================================================================================
# Lesson 58
# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------
# print(1, 2, 3, 4)
# print("hello", "I'm ahmed" , "and this first time" , int(4), sep="\n" , end="||")
# myList = [1, 2, 3, 5]
# print(myList)
# print(*myList)
# def say_hello(*peoples):  # n1, n2, n3, n4
#   for name in peoples:
#     print(f"Hello {name}")
# say_hello("Osama", "Ahmed", "Sayed", "Mahmoud")
# def show_details(name, *skills):
#   print(f"Hello {name} Your Skills Is: ")
#   for skill in skills:
#     print(skill)
# show_details("Osama", "Html", "CSS", "JS")
# show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")
# ==================================================================================
# Lesson 59
# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------
# def say_hello(name="Unknown", age="Unknown", country="Unknown"):  # default parameters must start from the end => can't set the first paramter to default value
#   print(f"Hello {name} Your Age is {age} and Your Country Is {country}")
# say_hello("Osama", 36, "Egypt")
# say_hello("Mahmoud", 28, "KSA")
# say_hello("Sameh", 38)
# say_hello("Ramy")
# say_hello()
# ==================================================================================
# Assignment 12
# 1
# def calculate(n1 , n2 , sign = "+"):
#   sign = sign.lower()
#   if sign == "+" or sign == "add" or sign == "a":
#     return n1 + n2
#   elif sign == "*" or sign == "multiply" or sign == "m":
#     return n2 * n1
#   elif sign == "-" or sign == "subtract" or sign == "s":
#     return n1 - n2
#   else:
#     return "worng choise"
# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "AdD")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30
# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10
# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200

# 2
# def addition(*xs):
#   res = 0
#   for x in xs:
#     if x == 10:
#       continue
#     elif x == 5:
#       res -= x
#     else:
#       res += x
#   return res
# print(addition(10, 20, 30, 10, 15)) # 65
# print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

# 3
# def show_skills(name,*skills):
#   if len(skills) == 0:
#     print(f"Hello {name} You have no skills to show")
#   else:
#     print(f"Hello {name} your skils is")
#     for skill in skills:
#       print(f"- {skill}")
# show_skills("Osama", "HTML", "CSS", "JS", "Python")
# show_skills("Ahmed")


# 4
# def say_hello(name ="UnKnown",age="UnKnown",county="Unknown"):
#   return f"Hello {name} Your Age Is {age} And You Live In {county}"
# print(say_hello("Osama", 38, "Egypt"))
# print(say_hello())
# ==================================================================================
# Lesson 60
# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------
# def show_skills(*skills):
#   print(type(skills)) # its a tuble
#   for skill in skills:
#     print(f"{skill}")
# show_skills("Html", "CSS", "JS")
# mySkills = {
#   'Html': "80%",
#   'Css': "70%",
#   'Js': "50%",
#   'Python': "80%",
#   "Go": "40%"
# }
# def show_skills(**skills):
#   print(type(skills)) # when its ** it just asking for a dictionary
#   for skill, value in skills.items():
#     print(f"{skill} => {value}")
# show_skills(**mySkills)
# show_skills(html = "40" , kss = "34" , mona = 27 , ahmed = 25)
# ==================================================================================
# Lesson 61
# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------
# myTuple = ("Html", "CSS", "JS")
# mySkills = {
#   'Go': "80%",
#   'Python': "50%",
#   'MySQL': "80%"
# }
# def show_skills(name, *skills, **skillsWithProgres):
#   print(f"Hello {name} \nSkills Without Progress Is: ")
#   for skill in skills:
#     print(f"- {skill}")
#   print("Skills With Progress Is: ")
#   for skill_key, skill_value in skillsWithProgres.items():
#     print(f"- {skill_key} => {skill_value}")
# show_skills("Osama", *myTuple, **mySkills)
# show_skills("mona","smart","beautful","kind",nur = "very good" , housWork = "suber good" , takingMyheart = "brilliant")
# ==================================================================================
# Lesson 62
# --------------------
# -- Function Scope --
# --------------------
# x = 1  # Global Scope
# def one():
#   global x # here we make x in a global scope not in a function scope only
#   x = 2
#   print(f"Print Variable From Function Scope {x}")
# def two():
#   x = 10
#   print(f"Print Variable From Function Scope {x}")
# one()
# print(f"Print Variable From Global Scope {x}")
# two()
# print(f"Print Variable From Global Scope After One Function Is Called {x}")
# ==================================================================================
# Lesson 63
# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------
# def cleanWord(word):
#   if len(word)  == 1:
#     return word
#   if word[0] == word[1]:
#     return cleanWord(word[1:])
#   return word[0] + cleanWord(word[1:])
# print(cleanWord("mmmmmmmmmmmmmmmooooooonnnaaaaaaaaaaaaaaa <<<<<<<<3333333"))
# ==================================================================================
# Lesson 64
# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------
# def say_hello(name, age):
#   return f"Hello {name} your Age Is: {age}"
# hello = lambda name, age: f"Hello {name} your Age Is: {age}"
# print(say_hello("Ahmed", 36))
# print(hello("Ahmed", 36))
# print(hello) #here the lambda function stored in variable and its return <function <lambda>
# print((lambda x: x**2)(2)) # (lambda var: var operation)(arguments)
# print(say_hello.__name__)
# print(hello.__name__)
# print(type(hello))
# ==================================================================================
# Assignment 13
# 1
# def get_score(**skills):
#   for skillKey , skillValue in skills.items():
#     print(f"{skillKey} => {skillValue}")
# get_score(Math=90, Science=80, Language=70)
# get_score(Logic=70, Problems=60)

# 2
# def get_people_scores(name="",**skills):
#   if len(skills) > 0:
#     if len(name) > 0:
#       print(f"Hello {name} This Is Your Score Table:")
#     for skillKey , skillValue in skills.items():
#       print(f"{skillKey} => {skillValue}")
#     print("=" *20)
#   else:
#     print(f"Hello {name} You Have No Scores To Show")
#     print("=" *20)
# get_people_scores("Osama", Math=90, Science=80, Language=70)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# get_people_scores(Logic=70, Problems=60)
# get_people_scores("Ahmed")

# 3
# scores_list = {
#   "Math" : 90,
#   "Science" : 80,
#   "Language" : 70
# }
# def get_the_scores(name="",**skills):
#     if len(skills) > 0:
#       if len(name) > 0:
#         print(f"Hello {name} This Is Your Score Table:")
#       for skillKey , skillValue in skills.items():
#         print(f"{skillKey} => {skillValue}")
#       print("=" *20)
#     else:
#       print(f"Hello {name} You Have No Scores To Show")
#       print("=" *20)
# get_the_scores("Osama", **scores_list)
# get_the_scores("Osama")
# get_the_scores(**scores_list)
# ==================================================================================


# ==================================================================================


# ==================================================================================


# ==================================================================================


# ==================================================================================


# ==================================================================================
