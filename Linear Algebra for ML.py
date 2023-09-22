# those laps from Corsera
#########Lap1###########
## NumPy to create 2-D arrays
# [1] NumPy(Numerical Python) is an open-source package that is widely used in science and engineering
# [2] After this assignment you will be able to:
"""   Use Jupyter Notebook and its features.
      Use NumPy functions to create arrays and NumPy array operations.
      Use indexing and slicing for 2-D arrays.
      Find the shape of an array, reshape it and stack it horizontally and vertically.
"""
# [3] Jupyter Notebooks are interactive coding journals that integrate live code, explanatory text, equations, visualizations and other multimedia resources, all in a single document
# =====================================================================================================
# 1 (Basics of NumPy) : its the main package for scientific computing in python
# =====================================================
# =========== 1.1- Packages
# import package as name
import numpy as np

# print(np.__version__)

# =========== 1.2- Advantages of using NumPy arrays
"""
NumPy library essential for organizing your data. You can think of them as a grid of values, all of the same type.
Python lists are limited in functions and take up more space and time to process than NumPy arrays.

NumPy provides an array object that is much faster and more compact than Python lists.
Through its extensive API integration, the library offers many built-in functions that make computing much easier with only a few lines of code.
This can be a huge advantage when performing math operations on large datasets.

The array object in NumPy is called ndarray meaning 'n-dimensional array'.
one of the most common array types: the one-dimensional array ('1-D').
A 1-D array represents a standard list of values entirely in one dimension.
Remember that in NumPy, all of the elements within the array are of the same type.
"""
# oneDimArr = np.array([10, 12])
# print(oneDimArr)

# =============== 1.3- How to create NumPy arrays
"""
There are several ways to create an array in NumPy.
You can create a 1-D array by simply using the function array() which takes in a list of values as an argument and returns a 1-D array.
"""
# x = np.array([1, 2, 3], dtype=float)
# print(x)
"""
Another way to implement an array is using np.arange().
This function will return an array of evenly spaced values within a given interval.
DOCSTRING
arange([start,] stop[, step,], dtype=None, *, like=None)
Return evenly spaced values within a given interval.
"""
# y = np.arange(4)  # from 0(default) to 3
# y1 = np.arange(2, 21, 3)
# print(y)
# print(y1)
"""
to create an array with five evenly spaced values in the interval from 0 to 100?
3 parameters that a function must take.
One paremeter is the starting number, in this case 0, the final number 100 and the number of elements in the array, in this case, 5.
NumPy has a function that allows you to do specifically this by using np.linspace().
"""
# # NumPyObjectName.linspace(a,b,x,dtype=...)
# lineSpacedArr = np.linspace(
#     100, 130, 3
# )  # returns an array of x number of "dtype"float(default) values(evenly spaced) in interval from a to b =>  [a,x,x,x,b]
# print(lineSpacedArr)  # the values returned is float(default)
# print(np.linspace(1, 12, 4, dtype=int))  # returns the same but the values are integers
# # NumPyObjectName.float64(values)
# print(np.float64([2, 3, 5]))  # returns float numbers
# charArr = np.array(["Welcome to my notes about linear algebra"])
# print(f"the array is: {charArr} and its type is: {charArr.dtype}")
# # here <U23 is that string is 23-character (23) unicode string (U) on a little-endian architecture (<)
# # and here everything (https://numpy.org/doc/stable/user/basics.types.html)

# =============== 1.4- More on NumPy arrays
"""
np.ones() - Returns a new array setting values to one.
np.zeros() - Returns a new array setting values to zero.
np.empty() - Returns a new uninitialized array.
np.random.rand() - Returns a new array with values chosen at random.
"""
# print(np.ones(4)) # returns array of shape 4 filled with ones
# print(np.zeros(3)) # same but with zeros
# print(np.empty(2)) # Return a new array of shape 3, without initializing entries.
# print(np.random.rand(3)) # Return a new array of shape 3 with random numbers between 0 and 1.
# print(np.random.randint(1,10,size=(3,4))) # Generate a 3 x 4 array of ints between 1 and 10

# ============########===============#################
# 2 (Multidimensional Arrays)
"""
With NumPy you can also create arrays with more than one dimension.
In the above examples, you dealt with 1-D arrays, where you can access their elements using a single index.
A multidimensional array has more than one column.
Think of a multidimensional array as an excel sheet where each row/column represents a dimension.
"""
# twoDimArr = np.array([[1, 2, 3], [4, 5, 6]])
# print(twoDimArr, "\n")
"""
An alternative way to create a multidimensional array is by reshaping the initial 1-D array.
Using np.reshape() you can rearrange elements of the previous array into a new shape.
"""
# oDimArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12])
# multiDimArr = np.reshape(oDimArr, (3, 4))
# print(multiDimArr, "\n")
# =====================================================
# =========== 2.1- Finding size, shape and dimension
"""
ndarray.ndim  - Stores the number dimensions of the array.
ndarray.shape - Stores the shape of the array. Each number in the tuple denotes the lengths of each corresponding dimension.
ndarray.size  - Stores the number of elements in the array.
"""
# print(multiDimArr.ndim) # return dim
# print(multiDimArr.shape) # return (rows,columns) => (m,n)
# print(multiDimArr.size) # return result of m*n

# ============########===============#################
# 3 (Array math operations)
"""
NumPy allows you to quickly perform elementwise addition, substraction, multiplication and division for both 1-D and multidimensional arrays.
The operations are performed using the math symbol for each '+', '-' and '*'.
Recall that addition of Python lists works completely differently as it would append the lists, 
thus making a longer list, in addition, subtraction and multiplication of Python lists do not work.
"""
# arr1 = np.array([2,4,6])
# arr2 = np.array([1,3,5])
# print(arr1 + arr2) # Addition
# print(arr2 - arr1) # Subtracting
# print(arr1 * arr2) # Muliplying
# =====================================================
# =========== 3.1- Multiplying vector with a scalar(broadcasting)
"""
NumPy computes each multiplication within each cell.
This concept is called broadcasting,
which allows you to perform operations specifically on arrays of different shapes.
"""
# vector = np.array([1,2])
# print(vector*3)

# ============########===============#################
# 4 (Indexing and slicing)
" it allows you to select specific elements from an array. It also lets you select entire rows/columns or planes"
# =====================================================
# =========== 4.1- Indexing
"1-D Array"
# onDim = [1, 2, 3, 4, 5]
# print(onDim[3],onDim[0])

"For multidimensional arrays of dim n, to go to specific elements you must input n indices"
# twDim = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(twDim, "\n")
# print(twDim[1][2]) # matrix[row][col] => ZERO Based

# =========== 4.1- Slicing
"Slicing gives you a sublist of elements that you specify from the array"
# array[start:end:step]
# onDim == onDim[:] == onDim[::]
# print(onDim[1:4], "\n")  # return subArray contains from index 1 to index 3 in 1-D
# print(twDim[0:1], "\n")  # return subArray contains the first row of the matrix 2-D
# print(twDim[2:], "\n")  # return subArray contains the last row of the matrix 2-D
# print(twDim[1:], "\n")  # return subArray contains the last two rows of the matrix 2-D
# print(twDim[:,2], "\n")  # return subArray contains the last col of the matrix 2-D
# print(twDim[:,0:2], "\n")  # return subArray contains the first two cols of the matrix 2-D

# ============########===============#################
# 5 (Stacking)
"""
It means to join two or more arrays, either horizontally or vertically, meaning that it is done along a new axis.
np.vstack() - stacks vertically
np.hstack() - stacks horizontally
np.hsplit() - splits an array into several smaller arrays
"""
# ar1 = np.array([[1,1],[2,2]])
# ar2 = np.array([[3,3],[4,4]])
# print(f"a1:\n{ar1}\n")
# print(f"a1:\n{ar2}\n")
# print(np.hstack((ar1,ar2)),"\n") # return a new array which put Arr1 next to Arr2[Arr1 Arr2]
# print(np.vstack((ar1,ar2)),"\n") # return a new array which put Arr1 at the top of Arr2
# print(np.hsplit(ar1,2))
# ============########===============#################==================########################==============
# ============########===============#################==================########################==============