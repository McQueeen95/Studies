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
### Lab 2 (Solving Linear Systems: 2 variables)
# ==========#######=========###
## 1 Representing and Solving System of Linear Equations using Matrices
# ==========#######====
# 1.1- System of Linear Equations
"is a collection of one or more linear equations involving the same variables."
# ==========#######====
# 1.2- solving Systems of Linear Equations using Matrices
"""
NumPy linear algebra package provides quick and reliable way to solve the system of linear equations using function np.linalg.solve(A, b).
Here A is a matrix, each row of which represents one equation in the system and each column corresponds to the variable x1, x2. And b
is a 1-D array of the free (right side) coefficients.
More information here (https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
so A is Coefficient matrix,  and b is the values of each equations, so [A|b] is augmented matrix
and Returns the Solution to the system
Return error if its singular(infinite solutions or no solution) or not square(n x !n)
"""
# a = np.array([
#       [-1,3],
#       [3,2]
# ])
# b = np.array([7,1])
# print("Matrix A:\n")
# print(a)
# print("\nValues b:\n")
# print(b,"\n")
# print(f"Shape of A: {a.shape}") # np.shape(a) its the same
# print(f"Size of A: {a.size}")
# print(f"Shape of b: {b.shape}")
# print(f"Size of A: {b.size}")
# print(f"Solution is: {np.int64(np.linalg.solve(a,b))}")
# ==========#######====
# 1.3- Evaluating Determinant of a Matrix
"""
In case of a square matrix it is possible to calculate its determinant.
System  will have one solution if and only if matrix A has non-zero determinant.
we can do it with the np.linalg.det(A) function.
"""
# a = np.array([
#       [1, 2],
#       [3, 4]
#       ])
# b = np.array([
#       [
#             [1, 2],
#             [3, 4]
#             ],
#       [
#             [1, 2],
#             [2, 1]
#             ],
#       [
#             [1, 3],
#             [3, 1]
#             ]
#       ])
# print(f"Det={np.linalg.det(a):.2f}")
# print(f"shape= {np.shape(b)}\n det= {np.linalg.det(b)}")
# ==========#######=========###
## 2 Solving System of Linear Equations using Elimination Method
# ==========#######====
" Programming approach can still help here to reduce the amount of arithmetical calculations, and focus on the method itself."
# 2.1- Elimination Method
"""
In the elimination method you either add or subtract the equations of the linear system to get an equation with smaller number of variables.
If needed, you can also multiply whole equation by non-zero number.
"""
# ==========#######====
# 2.2- Preparation for the Implementation of Elimination Method in the Code
# x = np.array([
#       [-1,3,7],
#       [3,2,1]
# ])
# print(x[1]) # this the second row
# ==========#######====
# 2.3- Implementation of Elimination Method
"""
first: copy the matrix to keep the original one
second: multiply first row by 3
third: add it to the second row
forth: exchange the second row with the result of this addition
"""
# xCopy = x.copy() # copying
# xCopy[1] = (3*xCopy[0] + xCopy[1])*1/11 # 3R1 + R2 --> R2
# print(xCopy)
# ==========#######====
# 2.4- Graphical Representation of the Solution
"""
the system of two equations there will be two lines corresponding to each of the equations,
and the solution will be the intersection point of those lines.
define a function plot_lines() to plot the lines and use it later to represent the solutions.
"""
# import matplotlib.pyplot as plt
# def plot_lines(M):
#       x_1 = np.linspace(-10, 10, 100)
#       x_2_line_1 = (M[0, 2] - M[0, 0] * x_1) / M[0, 1]
#       x_2_line_2 = (M[1, 2] - M[1, 0] * x_1) / M[1, 1]

#       _, ax = plt.subplots(figsize=(10, 10))
#       ax.plot(
#             x_1,
#             x_2_line_1,
#             "-",
#             linewidth=2,
#             color="#0075ff",
#             label=f"$x_2={-M[0,0]/M[0,1]:.2f}x_1 + {M[0,2]/M[0,1]:.2f}$",
#       )
#       ax.plot(
#             x_1,
#             x_2_line_2,
#             "-",
#             linewidth=2,
#             color="#ff7300",
#             label=f"$x_2={-M[1,0]/M[1,1]:.2f}x_1 + {M[1,2]/M[1,1]:.2f}$",
#       )

#       A = M[:, 0:-1]
#       b = M[:, -1::].flatten()
#       d = np.linalg.det(A)

#       if d != 0:
#             solution = np.linalg.solve(A, b)
#             ax.plot(
#             solution[0],
#             solution[1],
#             "-o",
#             mfc="none",
#             markersize=10,
#             markeredgecolor="#ff0000",
#             markeredgewidth=2,
#             )
#             ax.text(
#             solution[0] - 0.25,
#             solution[1] + 0.75,
#             f"$(${solution[0]:.0f}$,{solution[1]:.0f})$",
#             fontsize=14,
#             )
#       ax.tick_params(axis="x", labelsize=14)
#       ax.tick_params(axis="y", labelsize=14)
#       ax.set_xticks(np.arange(-10, 10))
#       ax.set_yticks(np.arange(-10, 10))

#       plt.xlabel("$x_1$", size=14)
#       plt.ylabel("$x_2$", size=14)
#       plt.legend(loc="upper right", fontsize=14)
#       plt.axis([-10, 10, -10, 10])

#       plt.grid()
#       plt.gca().set_aspect("equal")

#       plt.show()
# plot_lines(x)
# ==========#######=========###
## 3 System of Linear Equations with No Solutions
# ==========#######====
# a = np.array([
#       [-1, 3],
#       [3, -9]
#       ])
# b = np.array([7,1])
# print(np.linalg.det(a)) #Det = 0 so its infinte or no solution

# try:
#       x_2 = np.linalg.solve(a, b)
# except np.linalg.LinAlgError as err:  # here we get that the system is singular
#       print(err)

# a2 = np.hstack((a,b.reshape(2,1)))  # reshape it to do the elimination method
# print(a2)

# a2Copy = a2.copy()
# a2Copy[1] = 3 * a2Copy[0] + a2Copy[1]
# print(a2Copy)

# plot_lines(a2Copy)

# ==========#######=========###
## 4 System of Linear Equations with Infinite Number of Solutions
# ==========#######====
# x = np.array([[-1,3,7],[3,-9,-21]])
# xCopy = x.copy()
# xCopy[1] = xCopy[0] * 3 + xCopy[1]
# print(xCopy)
# plot_lines(xCopy)
# ============########===============#################==================########################==============
# ============########===============#################==================########################==============
### Lab 3 (Solving Linear Systems: 3 variables)
# ==========#######=========###
## 1 Representing and Solving System of Linear Equations using Matrices
# ==========#######====
# 1.1- System of Linear Equations
"is a collection of one or more linear equations involving the same variables."
# ==========#######====
# 1.2- Solving Systems of Linear Equations using Matrices
"each row will represent one equation and each column correspond to x1,x2,x3 var and b is the coefficients"
# A = np.array([
#         [4, -3, 1],
#         [2, 1, 3],
#         [-1, 2, -5]
#     ], dtype=np.dtype(int))
# b = np.array([-10, 0, 17], dtype=np.dtype(int))
# print(f"the solution of the matrix is: {np.int64(np.linalg.solve(A,b))}")
# ==========#######====
# 1.3- Evaluating the Determinant of a Matrix
"if its a square matrix it is possible to get its determinant ==> np.linalg.det(array)"
# print(f"Det = {np.linalg.det(A):.1f}")
# ==========#######=========###
## 2 Solving System of Linear Equations using Row Reduction
# ==========#######====
# 2.1- Preparation for Row Reduction
"that way u can practice some solution techniques manually"
"to use A and b matrix and make them agumented matrix [A|b]"
# matrixA = np.hstack((A,b.reshape(3,1)),dtype=float) # original shape:(3,) , we make it (3,1)
# print(matrixA) # we need to transform it so that it has the same number of dimensions
# ==========#######====
# 2.2- Functions for Elementary Operations
"""
elementary operations:
  - Multiply any row by a non-zero number
  - Add two rows and exchange one of the original rows with the result of the addition
  - Swap rows
"""
def multiplyRow(matrix,rowNum,multiplyNum):
  indexedRowNum = rowNum -1
  if multiplyNum == 0:
    return "Error enter non-zero value"
  Nmatrix = matrix.copy()
  Nmatrix[indexedRowNum] = Nmatrix[indexedRowNum] * multiplyNum
  return Nmatrix

def multiplyAndAddRows(matrix,rowNum1,rowNum2,rowNum1Multiple):# xR1 + R2 --> R2
  indexedRowNum1 = rowNum1 -1
  indexedRowNum2 = rowNum2 -1
  if rowNum1Multiple == 0:
    return "Error enter non-zero value"
  Nmatrix = matrix.copy()
  Nmatrix[indexedRowNum2] = rowNum1Multiple * Nmatrix[indexedRowNum1] + Nmatrix[indexedRowNum2]
  return Nmatrix

def swapRows(matrix,rowNum1,rowNum2):
  indexedRowNum1 = rowNum1 -1
  indexedRowNum2 = rowNum2 -1
  Nmatrix = matrix.copy()
  Nmatrix[[indexedRowNum1,indexedRowNum2]] = Nmatrix[[indexedRowNum2,indexedRowNum1]] # matrix[x][y] = matrix[x,y] R the same
  return Nmatrix

def giveMeInRowReduction3_4(matrix):
  matrix = multiplyRow(matrix,3,1/matrix[2,2])
  X3 = matrix[2][3]
  X2 = (matrix[1,3] - matrix[1,2] * X3) / matrix[1,1]
  X1 = (matrix[0,3] - matrix[0,2] * X3 - matrix[0,1] * X2) / matrix[0,0]
  print(f"X1= {X1}\nX2= {X2}\nX3= {X3}")

# print(f"by applying: 2*R3 --> R3 \n the matrix is:\n{multiplyRow(matrixA,3,2)}")
# print(f"by applying: 1/2*R2 + R3 --> R3 \n the matrix is:\n{multiplyAndAddRows(matrixA,2,3,1/2)}")
# print(f"by applying: R1 <--> R3 \n the matrix is:\n{swapRows(matrixA,1,3)}")

# ==========#######====
# 2.3- Row Reduction and Solution of the Linear System
# A_ref = swapRows(matrixA,1,3) # R1 <--> R3
# A_ref = multiplyAndAddRows(A_ref,1,2,2) # 2*R1 + R2 --> R2
# A_ref = multiplyAndAddRows(A_ref,1,3,4) # 4*R1 + R3 --> R3
# A_ref = multiplyAndAddRows(A_ref,2,3,-1) # -1*R2 + R3 --> R3
# print(A_ref) # now its on Row Reduction form
# giveMeInRowReduction3_4(A_ref)

# we use the same methods with No solutions and infinite number of solutions
# np.linalg.solve gives an error if there are no or infinitely many solutions,

# ============########===============#################==================########################==============
# ============########===============#################==================########################==============
### Lab 3

