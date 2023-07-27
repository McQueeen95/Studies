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
