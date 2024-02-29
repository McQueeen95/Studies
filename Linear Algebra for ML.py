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
import matplotlib.pyplot as plt
import time
import cv2  # openCV library for image transformations.

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
# print(oneDimArr, "\n",np.array([[10],[12]]),"\n",np.array([[10,12]]),"\n")

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
# print(np.arange(0,101,25))
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
# """
# oDimArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12])
# multiDimArr = np.reshape(oDimArr, # the array to be reshaped
#                         (3, 4) # dimensions of the new array
#                         )
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
# print(twDim[2:], "\n")  # return subArray contains the last row of the matrix 2-D ==> [[a,b,c]]
# print(twDim[2], "\n")  # return subArray contains the last row of the matrix 2-D  ==> [a,b,c]
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
# print(np.hsplit(ar1,2)) # split the array into 2 subarrays of equal size
# print(np.hsplit(ar2,[1])) # split the array after the first column
# print(np.hsplit(ar2,[1,3])) # split the array after the first and the third row
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
#       ],
#       [
#             [1, 2],
#             [2, 1]
#       ],
#       [
#             [1, 3],
#             [3, 1]
#       ]
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
def multiplyRow(matrix, rowNum, multiplyNum):
    indexedRowNum = rowNum - 1
    if multiplyNum == 0:
        return "Error enter non-zero value"
    Nmatrix = matrix.copy()
    Nmatrix[indexedRowNum] = Nmatrix[indexedRowNum] * multiplyNum
    return Nmatrix
def multiplyAndAddRows(matrix, rowNum1, rowNum2, rowNum1Multiple):  # xR1 + R2 --> R2
    indexedRowNum1 = rowNum1 - 1
    indexedRowNum2 = rowNum2 - 1
    if rowNum1Multiple == 0:
        return "Error enter non-zero value"
    Nmatrix = matrix.copy()
    Nmatrix[indexedRowNum2] = (
        rowNum1Multiple * Nmatrix[indexedRowNum1] + Nmatrix[indexedRowNum2]
    )
    return Nmatrix
def swapRows(matrix, rowNum1, rowNum2):
    indexedRowNum1 = rowNum1 - 1
    indexedRowNum2 = rowNum2 - 1
    Nmatrix = matrix.copy()
    Nmatrix[[indexedRowNum1, indexedRowNum2]] = Nmatrix[
        [indexedRowNum2, indexedRowNum1]
    ]  # matrix[x][y] = matrix[x,y] R the same
    return Nmatrix
def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.
    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.
    Returns:
    int or None: The index of the first non-zero value in the specified column, starting from the given row.
                Returns None if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:,column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array. 
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol = 1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return None.
    return None
def get_index_first_non_zero_value_from_row(M, row): # gitting the index of pivot
    """
    Find the index of the first non-zero value in the specified row of the given matrix.
    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - row (int): The index of the row to search.
    Returns:
    int or None: The index of the first non-zero value in the specified row.
                Returns None if no non-zero value is found.
    """
    # Get the desired row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns None.
        if not np.isclose(val, 0, atol = 1e-5):
            return i
    return None
def giveMeInRowReduction3_4(matrix):
    matrix = multiplyRow(matrix, 3, 1 / matrix[2, 2])
    X3 = matrix[2][3]
    X2 = (matrix[1, 3] - matrix[1, 2] * X3) / matrix[1, 1]
    X1 = (matrix[0, 3] - matrix[0, 2] * X3 - matrix[0, 1] * X2) / matrix[0, 0]
    print(f"X1= {X1}\nX2= {X2}\nX3= {X3}")
def giveMeInRowReduction4_5(mat):
    mat = multiplyRow(mat, 4, 1 / mat[3, 3])
    X4 = mat[3, 4]
    X3 = (mat[2, 4] - mat[2, 3] * X4) / mat[2, 2]
    X2 = (mat[1, 4] - mat[1, 2] * X3 - mat[1, 3] * X4) / mat[1, 1]
    X1 = (mat[0, 4] - mat[0, 1] * X2 - mat[0, 2] * X3 - mat[0, 3] * X4) / mat[0, 0]
    print(f"X1= {X1}\nX2= {X2}\nX3= {X3}\nX4= {X4}")
def move_row_to_bottom(M, row_index):
    """
    Move the specified row to the bottom of the given matrix.
    Parameters:
    - M (numpy.array): Input matrix.
    - row_index (int): Index of the row to be moved to the bottom.
    Returns:
    - numpy.array: Matrix with the specified row moved to the bottom.
    """
    # Make a copy of M to avoid modifying the original matrix
    M = M.copy()
    # Extract the specified row
    row_to_move = M[row_index]
    # Delete the specified row from the matrix
    M = np.delete(M, row_index, axis=0)
    # Append the row at the bottom of the matrix
    M = np.vstack([M, row_to_move])
    return M
def augmented_matrix(A, B):
    """
    Create an augmented matrix by horizontally stacking two matrices A and B.
    Parameters:
    - A (numpy.array): First matrix.
    - B (numpy.array): Second matrix.
    Returns:
    - numpy.array: Augmented matrix obtained by horizontally stacking A and B.
    """
    return np.hstack((A,B))
def reduced_row_echelon_form(A, B):
    """
    Utilizes elementary row operations to transform a given set of matrices,
    which represent the coefficients and constant terms of a linear system,
    into reduced row echelon form.
    Parameters:
    - A (numpy.array): The input square matrix of coefficients.
    - B (numpy.array): The input column matrix of constant terms
    Returns:
    numpy.array: A new augmented matrix in reduced row echelon form.
    """
    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()
    # Convert matrices to float to prevent integer division
    A = A.astype('float64')
    B = B.astype('float64')
    # Number of rows in the coefficient matrix
    num_rows = len(A)
    # List to store rows that should be moved to the bottom (rows of zeroes)
    rows_to_move = []
    # Transform matrices A and B into the augmented matrix M
    M = np.hstack((A, B))
    # Iterate over the rows.
    for i in range(num_rows):
        # Find the first non-zero entry in the current row (pivot)
        pivot = next((val for val in M[i, i:] if not np.isclose(val, 0)), 0)
        # This variable stores the pivot's column index, it starts at i,
        # but it may change if the pivot is not in the main diagonal.
        column_index = i
        # CASE PIVOT IS ZERO
        if np.isclose(pivot, 0):
            # PART 1: Look for rows below the current row to swap,
            # you may use the function get_index_first_non_zero_value_from_column
            # index = np.argmax(np.abs(M[i:, i])) + i
            index = get_index_first_non_zero_value_from_column(M, column_index, i)
            # If there is a non-zero pivot
            if index is not None:
                # Swap rows if a non-zero entry is found below the current row
                # M[[i, index]] = M[[index, i]]
                swapRows(M, i + 1, index + 1)
                # Update the pivot after swapping rows
                pivot = M[i, i]
            # PART 2 - NOT GRADED. This part deals with the case where
            # the pivot isn't in the main diagonal.
            # If no non-zero entry is found below it to swap rows,
            # then look for a non-zero pivot outside the diagonal.
            if index is None:
                index_new_pivot = get_index_first_non_zero_value_from_row(M, i) 
                # If there is no non-zero pivot, it is a row with zeroes,
                # save it into the list rows_to_move so you can move it to the bottom further.
                # The reason for not moving right away is that it would mess up the indexing in the for loop.
                # The second condition i >= num_rows is to avoid taking the augmented part into consideration.
                if index_new_pivot is None or index_new_pivot >= num_rows:
                    rows_to_move.append(i)
                    continue
                # If there is another non-zero value outside the diagonal, it will be the pivot.
                else:
                    pivot = M[i, index_new_pivot]
                    # Update the column index to agree with the new pivot position
                    column_index = index_new_pivot
        # END HANDLING FOR PIVOT 0
        # Divide the current row by the pivot, so the new pivot will be 1. (reduced row echelon form)
        M[i] = M[i] / pivot
        # Perform row reduction for rows below the current row
        for j in range(i + 1, num_rows):
            # Get the value in the row that is below the pivot value.
            # Remember that the value in the column position is given
            # by the variable called column_index
            value_below_pivot = M[j, column_index]
            # Perform row reduction using the formula:
            # row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row
            M[j] = M[j] - value_below_pivot * M[i]
    # Move every row of zeroes to the bottom
    for row_index in rows_to_move:
        M = np.concatenate((M[:row_index], M[row_index + 1:], M[row_index:row_index + 1]))
    return M
def check_solution(M):
    """
    Given an augmented matrix in reduced row echelon form, determine the nature of the associated linear system.
    Parameters:
    - M (numpy.array): An (n x n+1) matrix representing the augmented form of a linear system,
    where n is the number of equations and variables
    Returns:
    - str: A string indicating the nature of the linear system:
    - "Unique solution." if the system has one unique solution,
    - "No solution." if the system has no solution,
    - "Infinitely many solutions." if the system has infinitely many solutions.
    This function checks for singularity and analyzes the constant terms to determine the solution status.
    """
    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()
    # Get the number of rows in the matrix
    num_rows = len(M)
    # Define the square matrix associated with the linear system
    coefficient_matrix = M[:,:-1]
    # Define the vector associated with the constant terms in the linear system
    constant_vector = M[:,-1]
    # Flag to indicate if the matrix is singular
    singular = False
    # Iterate over the rows of the coefficient matrix
    for i in range(num_rows):
        # Test if the row from the square matrix has only zeros (do not replcae the part 'is None')
        if get_index_first_non_zero_value_from_row(coefficient_matrix, i) is None:
            # The matrix is singular, analyze the corresponding constant term to determine the type of solution
            singular = True 
            # If the constant term is non-zero, the system has no solution
            if not np.isclose(constant_vector[i],0):
                return "No solution." 
    # Determine the type of solution based on the singularity condition            
    if singular:        
        return "Infinitely many solutions."
    else:
        return "Unique solution."
def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.
    Parameters:
    - M (numpy.array): The augmented matrix in reduced row echelon form (n x n+1).
    Returns:
    numpy.array: The solution vector of the linear system.
    """
    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()
    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = len(M)
    # Iterate from bottom to top
    for i in range(num_rows-1,-1,-1):
        # Get the substitution row
        substitution_row = M[i,:]
        # Iterate over the rows above the substitution_row
        for j in range(i-1,-1,-1):
            # Get the row to be reduced
            row_to_reduce = M[j,:]
            # Get the index of the first non-zero element in the substitution row
            index = get_index_first_non_zero_value_from_row(M, i)
            # Get the value of the element at the found index
            value = row_to_reduce[index]
            # Perform the back substitution step using the formula row_to_reduce = None
            row_to_reduce = row_to_reduce - value * substitution_row
            # Replace the updated row in the matrix
            M[j, :] = row_to_reduce
    # Extract the solution from the last column
    solution = M[:,-1]
    return solution
def gaussian_elimination(A, B):
    """
    Solve a linear system represented by an augmented matrix using the Gaussian elimination method.
    Parameters:
    - A (numpy.array): Square matrix of size n x n representing the coefficients of the linear system
    - B (numpy.array): Column matrix of size 1 x n representing the constant terms.
    Returns:
    numpy.array or str: The solution vector if a unique solution exists, or a string indicating the type of solution.
    """
    ### START CODE HERE ###
    # Get the matrix in row echelon form
    reduced_row_echelon_M = reduced_row_echelon_form(A,B)
    # Check the type of solution (unique, infinitely many, or none)
    solution = check_solution(reduced_row_echelon_M)
    # If the solution is unique, perform back substitution
    if solution == "Unique solution.": 
        solution = back_substitution(reduced_row_echelon_M)
    ### END SOLUTION HERE ###
    return solution


# A = np.array([[2,1,5],[1,3,1], [3,4,6]])
# B = np.array([[0], [0], [0]])
# print(reduced_row_echelon_form(A,B))
# print(np.linalg.det(A))
# print(gaussian_elimination(A,B))
# print(back_substitution(reduced_row_echelon_form(A,B)))
# print(np.linalg.solve(A,B))
# matrix = np.hstack((A,np.reshape(B,(3,1)))) # make it agumented matrix
# print(check_solution(reduced_row_echelon_form(A,B)))
# print(f"by applying: 2*R3 --> R3 \n the matrix is:\n{multiplyRow(matrixA,3,2)}")
# print(f"by applying: 1/2*R2 + R3 --> R3 \n the matrix is:\n{multiplyAndAddRows(matrixA,2,3,1/2)}")
# print(f"by applying: R1 <--> R3 \n the matrix is:\n{swapRows(matrixA,1,3)}")
# N = np.array([
# [0, 5, -3 ,6 ,8],
# [0, 6, 3, 8, 1],
# [0, 0, 0, 0, 0],
# [0, 0, 0 ,1 ,7],
# [0, 2, 1, 0, 4]
# ]
# )
# print(N)
# print(get_index_first_non_zero_value_from_column(N, column = 1, starting_row = 2))
# print(f'Output for row 2: {get_index_first_non_zero_value_from_row(N, 2)}')
# print(f'Output for row 3: {get_index_first_non_zero_value_from_row(N, 3)}')
# M = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(f'Matrix before:\n{M}')
# print(f'Matrix after moving index 1:\n{move_row_to_bottom(M, 1)}')
# A = np.array([[1,9,3], [3,4,5], [4,5,6]])
# B = np.array([[1], [85], [7]])
# print(gaussian_elimination(A,B))
# print(back_substitution(reduced_row_echelon_form(A,B)))
# print(np.linalg.solve(A,B))
# print(augmented_matrix(A,B))
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
### Assignment 1
# A = np.array([
#   [2,-1,1,1],
#   [1,2,-1,-1],
#   [-1,2,2,2],
#   [1,-1,2,1]
# ],dtype=np.dtype(float))
# b =np.array([6,3,14,8],dtype=np.dtype(float))
# d = np.linalg.det(A)
# print(f"{d:.2f}") # determant
# x = np.linalg.solve(A,b)
# print(x) # solving the system
# matrix = np.hstack((A,np.reshape(b,(4,1)))) # make it agumented matrix
# mat = swapRows(matrix,1,2)
# mat = multiplyAndAddRows(mat,1,2,-2)
# mat = multiplyAndAddRows(mat,1,3,1)
# mat = multiplyAndAddRows(mat,1,4,-1)
# mat = multiplyAndAddRows(mat,3,4,1)
# mat = swapRows(mat,2,4)
# mat = multiplyAndAddRows(mat,3,4,1)
# mat = multiplyAndAddRows(mat,2,3,-4)
# mat = multiplyAndAddRows(mat,2,4,1)
# mat = multiplyAndAddRows(mat,4,3,2)
# mat = multiplyAndAddRows(mat,3,4,-8)
# mat = multiplyRow(mat,4,-1/17)
# print(mat) # this in row echelon form
# giveMeInRowReduction4_5(mat)
# mat = multiplyAndAddRows(mat,4,3,-3)
# mat = multiplyAndAddRows(mat,4,2,-3)
# mat = multiplyAndAddRows(mat,4,1,1)
# mat = multiplyAndAddRows(mat,3,2,-4)
# mat = multiplyAndAddRows(mat,3,1,1)
# mat = multiplyAndAddRows(mat,2,1,-2)
# print(mat) # this in reduced row echlon form
#######################################
# A = np.array(
#     [
#         [1,1,-1],
#         [1,-1,2],
#         [4,-2,1]
#     ],dtype=np.dtype(float)
# )
# b = np.array([6,4,10],dtype=np.dtype(float))
# print(np.linalg.det(A))
# print(np.linalg.solve(A,b))
# A = np.array([[1,2,3],[0,0,0], [0,0,5]])
# B = np.array([[1], [2], [4]])
# matrix = np.hstack((A,np.reshape(B,(3,1)))) # make it agumented matrix
# print(augmented_matrix(A, B) , '\n',np.hstack((A,B)))
# mat = multiplyAndAddRows(matrix,1,2,-1)
# mat = multiplyAndAddRows(mat,1,3,-4)
# mat = multiplyAndAddRows(mat,2,3,-3)
# mat = multiplyAndAddRows(mat,3,1,-1/4)
# mat = multiplyRow(mat,3,1/4)
# mat = multiplyAndAddRows(mat,3,2,3)
# mat = multiplyAndAddRows(mat,2,1,1/2)
# mat = multiplyRow(mat,2,-1/2)
# giveMeInRowReduction3_4(mat)
# ============########===============#################==================########################==============
# ============########===============#################==================########################==============
### Lab 4 (Vector Operations: Scalar Multiplication, Sum and Dot Product of Vectors)
# ==========#######=========###
## 1- Scalar Multiplication and Sum of Vectors
"every vector written here is Trasposed to a column vector"
# ======####==
# 1.1 Visualization of a Vector (𝑣 ∈ ℝ2) R2 is a plane in two dimension
"We can see that vectors can be visualized as arrows in the plane"
def plot_vectors(list_v, list_label, list_color):
    _, ax = plt.subplots(figsize=(10, 10))
    ax.tick_params(axis="x", labelsize=14)
    ax.tick_params(axis="y", labelsize=14)
    ax.set_xticks(np.arange(-10, 10))
    ax.set_yticks(np.arange(-10, 10))
    plt.axis([-10, 10, -10, 10])
    for i, v in enumerate(list_v):
        sgn = 0.4 * np.array([[1] if i == 0 else [i] for i in np.sign(v)])
        plt.quiver(
            v[0], v[1], color=list_color[i], angles="xy", scale_units="xy", scale=1
        )
        ax.text(
            v[0] - 0.2 + sgn[0],
            v[1] - 0.2 + sgn[1],
            list_label[i],
            fontsize=14,
            color=list_color[i],
        )
    plt.grid()
    plt.gca().set_aspect("equal")
    plt.show()
# v = np.array([[1],[3]])
# w = np.array([[4],[-1]])
# n= np.array([0,9])
# s= np.array([9,0])
# e = np.array([0,-9])
# d = np.array([-9,0])
# plot_vectors([v], ["v"], ["gray"]) # drawing a vector from (0,0) to (1,3)
# ======####==
# 1.2 Scalar Multiplication
"""
    Scalar multiplication of a vector 𝑣 =[ 𝑣1 𝑣2 … 𝑣𝑛] ∈ ℝ𝑛 by a scalar 𝑘 is a vector  𝑘𝑣=[𝑘𝑣1 𝑘𝑣2 … 𝑘𝑣𝑛] (element by element multiplication).
    If  𝑘>0 , then  𝑘𝑣 is a vector pointing in the same direction as 𝑣 and it is 𝑘 times as long as 𝑣
    If  𝑘=0 , then  𝑘𝑣is a zero vector.
    If  𝑘<0 , vector  𝑘𝑣 will be pointing in the opposite direction.
    In Python you can perform this operation with a * operator.
"""
# plot_vectors([v, 2*v, -2*v , 0*v], [f"$v$", "2v", "-2v",f"$0v$"], ["brown", "green", "blue","black"])
# ======####==
# 1.3 Sum of Vectors
"""
    Sum of vectors (vector addition) can be performed by adding the corresponding components of the vectors:
    if  𝑣 =[ 𝑣1 𝑣2 … 𝑣𝑛] ∈ ℝ𝑛 and 𝑤 = [ 𝑤1 𝑤2 … 𝑤𝑛] ∈ ℝ𝑛 , then  𝑣+𝑤 = [ 𝑣1+𝑤1 𝑣2+𝑤2 … 𝑣𝑛+𝑤𝑛 ] ∈ ℝ𝑛. 
    The so-called parallelogram law gives the rule for vector addition. 
    For two vectors  𝑢 and  𝑣
    represented by the adjacent sides (both in magnitude and direction) of a parallelogram drawn from a point, the vector sum  𝑢+𝑣
    is is represented by the diagonal of the parallelogram drawn from the same point
    In Python you can either use + operator or NumPy function np.add().
"""
# plot_vectors([v, w, v + w], [f"$v$", f"$w$", f"$v + w$"], ["black", "black", "red"]) # v + w == np.add(v, w)
# plot_vectors([n, s ,e,d ,n+s , s+e , e+d, d+n], [f"$n$", f"$s$",f"$e$",f"$d$",f"$n+s$",f"$s+e$",f"$e+d$",f"$d+n$"], ["black", "black","black","black","red", "red","red","red"])
# ======####==
# 1.4 Norm of Vector
"""
    The norm of a vector  𝑣 is denoted as  |𝑣|. 
    It is a nonnegative number that describes the extent of the vector in space (its length). 
    The norm of a vector can be found using NumPy function np.linalg.norm()
"""
# print("Norm of a vector v is", np.linalg.norm(v))
# print("Norm of a vector d is", np.linalg.norm(d))
# ==========#######=========###
## 2- Dot Product
# ======####==
# 2.1  Algebraic Definition of the Dot Product
"""
    The dot product (or scalar product) is an algebraic operation that takes two vectors  𝑥 = [ 𝑥1 𝑥2 … 𝑥𝑛] ∈ ℝ𝑛 and 𝑦 = [ 𝑦1 𝑦2 … 𝑦𝑛] ∈ ℝ𝑛 and returns a single scalar. 
    The dot product can be represented with a dot operator  𝑥 ⋅ 𝑦 (x dot y)
    and defined as: 𝑥 ⋅ 𝑦 = ∑(1 => n) 𝑥𝑖*𝑦𝑖 = 𝑥1*𝑦1 + 𝑥2*𝑦2 + … + 𝑥𝑛*𝑦𝑛
"""
# ======####==
# 2.2 Dot Product using Python
"Note: it is recommended to define vectors as NumPy arrays to avoid errors."
def Vdot2(x, y):
    return sum(x[i] * y[i] for i in range(len(x)))
def Vdot1(x, y):
    sum = 0
    for xi, yi in zip(x, y):
        sum += xi * yi
    return sum
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# all the methods below give the same result but they are different in terms of speed
# print(x.dot(y))  # 32 (vectorized form)
# print(np.dot(x, y))  # 32 (vectorized form)
# print(x @ y)  # 32 (vectorized form)
# print(Vdot1(x, y))  # 32 (loop form)
# print(Vdot2(x, y))  # 32 (loop form)
# ======####==
## 2.3 Speed of Calculations in Vectorized Form
"""
    It is important to understand the difference in the speed of calculations using vectorized and the loop forms of the vectors and functions. 
    In the loop form operations are performed one by one, while in the vectorized form they can be performed in parallel. 
    In the section above you defined loop version of the dot product calculation (function Vdot1() and VdotProduct()), while np.dot(), @ and x.dot(y) are the functions representing vectorized form.
    Let's perform a simple experiment to compare their speed by using time.time() function to evaluate amount of time (in seconds) required to calculate dot product using the function Vdot(x,y). 
    Define new vectors  𝑎 and  𝑏 of the same size 1,000,000
"""
# a = np.random.rand(1000000)
# b = np.random.rand(1000000)
# "now we gonna compare the speed of all those methods"

# tic = time.time()
# operation = Vdot1(a, b)
# toc = time.time()
# print("result:  {:.2f}".format(operation))
# print("loop version: {:.2f} ms\n".format(1000 * (toc - tic)))

# tic = time.time()
# operation = Vdot2(a, b)
# toc = time.time()
# print("result:  {:.2f}".format(operation))
# print("loop version: {:.2f} ms\n".format(1000 * (toc - tic)))

# tic = time.time()
# operation = a.dot(b)
# toc = time.time()
# print("result:  {:.2f}".format(operation))
# print("vectorized version: {:.2f} ms\n".format(1000 * (toc - tic)))

# tic = time.time()
# operation = np.dot(a,b)
# toc = time.time()
# print("result:  {:.2f}".format(operation))
# print("vectorized version: {:.2f} ms\n".format(1000 * (toc - tic)))

# tic = time.time()
# operation = a @ b
# toc = time.time()
# print("result:  {:.2f}".format(operation))
# print("vectorized version:{:.2f} ms\n".format(1000 * (toc - tic)))

# ======####==
# 2.4 Geometric Difinition of the Dot Product
"""
    a Euclidean vector has both magnitude and direction. 
    The dot product of two vectors  𝑥 and  𝑦 is defined by: 𝑥 ⋅ 𝑦 = |𝑥| |𝑦| cos(𝜃), where  𝜃 is the angle between the two vectors
    if the two vectrors are orthogonal, the angle between them is 0, and the dot product is 0.
"""
# i = np.array([1, 0, 0])
# j = np.array([0, 1, 0])
# print("The dot product of i and j is", Vdot1(i, j))
# ======####==
# 2.5 Application of the Dot Product: Vector Similarity
"""
    Geometric definition of a dot product is used in one of the applications - to evaluate vector similarity.
    In Natural Language Processing (NLP) words or phrases from vocabulary are mapped to a corresponding vector of real numbers.
    Similarity between two vectors can be defined as a cosine of the angle between them. 
    When they point in the same direction, their similarity is 1 and it decreases with the increase of the angle.
    Then we use to evaluate cosine of the angle between vectors: cos(𝜃) = ( 𝑥 ⋅ 𝑦 )/( |𝑥| |𝑦| )
    Zero value corresponds to the zero similarity between vectors (and words corresponding to those vectors).
    Largest value is when vectors point in the same direction, lowest value is when vectors point in the opposite directions.
    This example of vector similarity is given to link the material with the Machine Learning applications.
"""
# ============########===============#################==================########################==============
# ============########===============#################==================########################==============
### Lab 5 (Matrix Multiplication)
# ==========#######=========###
## 1- Matrix Multiplication using Python
"we gonna show the most commonly used function in the vectorized form"
# A = np.array([[4, 9, 9], [9, 1, 6], [9, 2, 3]])
# print("Matrix A (3 by 3):\n", A)
# B = np.array([[2, 2], [5, 7], [4, 4]])
# print("Matrix B (3 by 2):\n", B)
"first function is np.matmul() , second is '@' and third is 'x.dot(y)'"
# print(np.matmul(A, B))
# print(A @ B)
# print(A.dot(B))
# ============
## 2- Matrix Conversion and Broadcasting
""" 
    matrix multiplication is defined only if number of the columns of matrix  𝐴
    is equal to the number of the rows of matrix  𝐵
    and if we try to code something like this it will give an error.
"""
# try:
#     np.matmul(B, A)
# except ValueError as err:
#     print(err)
"so the number of the columns in the first matrix should match the number of the rows in the second matrix"
# backing to multipliying of the vectors there's a strange shortcut that I gonna show it to u
# x = np.array([1, -2, -5])
# y = np.array([4, 3, -1])
# print("Shape of vector x:", x.shape)
# print("Number of dimensions of vector x:", x.ndim)
# print("Shape of vector x, reshaped to a matrix:", x.reshape((3, 1)).shape)
# print("Number of dimensions of vector x, reshaped to a matrix:", x.reshape((3, 1)).ndim)
# from we know when we multiply x by y it will give us an error
# print(np.matmul(x,y)) # here we try without any reshape
# but it worked fine!!! , so how ?
"So, vector  𝑥 was automatically transposed into the vector  1×3 and matrix multiplication  𝑥𝑇 𝑦 was calculate   d."  # xT is x transpose
# now we gonna try same thing but now with reshape
# try:
#     np.matmul(x.reshape((3, 1)), y.reshape((3, 1)))
# except ValueError as err:
#     print(err)
"""
    and this gives an error, 
    so we now know that python is smart enough to understand that the number of the columns in the first matrix should match the number of the rows in the second matrix
    as we can see that he trasposed x by himself to fit the multiplication rule
    What actually happens is what is called broadcasting in Python:
    NumPy broadcasts this dot product operation to all rows and all columns, 
    you get the resultant product matrix.
"""
# and this is good and bad at the same time , let me show to u:
# print(A - 2)
"""
    Mathematically, subtraction of the 3×3 matrix  𝐴 and a scalar is not defined,
    but Python broadcasts the scalar, creating a  3×3 np.array and performing subtraction element by element.
"""
# ============########===============#################==================########################==============
# ============########===============#################==================########################==============
#!## Lab 6 (Linear Transformations)
# * In this lab you will explore linear transformations, visualize their results and master matrix multiplication to apply various linear transformations.
# ==========#######=========###
#!# 1- Transformations
"""
    A transformation is a function from one vector space to another that respects the underlying (linear) structure of each vector space. 
    Referring to a specific transformation, you can use a symbol, such as  𝑇.
    Specifying the spaces containing the input and output vectors, e.g.  ℝ2 and  ℝ3, you can write  𝑇:ℝ2→ℝ3.
    Transforming vector  𝑣∈ℝ2 into the vector  𝑤∈ℝ3 by the transformation  𝑇, you can use the notation  𝑇(𝑣)=𝑤
    and read it as "T of v equals to w" or "vector w is an image of vector v with the transformation T".
    The following Python function corresponds to the transformation  𝑇:ℝ2→ℝ3 with the following symbolic formula:
    T([𝑣1 𝑣2])= [3*𝑣1 0 -2*𝑣2]        ==>   (1)
"""
def T(v):
    w = np.zeros((3, 1))
    w[0, 0] = 3 * v[0, 0]  # W[row,column]
    w[2, 0] = -2 * v[1, 0]  # W[row = 2, column = 0]
    return w
# here the the second row is still zero as we didn't specify it
# v = np.array([[3], [5]])
# w = T(v)
# print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)
# ============
#!# 2- Linear Transformations
"""
A transformation 𝑇 is said to be linear if the following two properties are true for any scalar 𝑘, and any input vectors 𝑢 and 𝑣:
*(1) 𝑇(𝑘𝑣)=𝑘𝑇(𝑣)
*(2) 𝑇(𝑢+𝑣)=𝑇(𝑢)+𝑇(𝑣)
"""
# u = np.array([[1], [-2]])
# v = np.array([[2], [4]])
# k = 7
# print("T(k*v):\n", T(k*v), "\n k*T(v):\n", k*T(v), "\n\n")
# print("T(u+v):\n", T(u+v), "\n T(u)+T(v):\n", T(u)+T(v))
# then we can see that the first and second property is true, so it is linear transformation
# ============
#!# 3- Transformations Defined as a Matrix Multiplication
"""
Let  𝐿:ℝ𝑚→ℝ𝑛 be defined by a matrix 𝐴, where  𝐿(𝑣)=𝐴𝑣, multiplication of the matrix 𝐴(𝑛×𝑚) and vector 𝑣(𝑚×1) resulting in the vector 𝑤(𝑛×1).
"""
def L(v):
    A = np.array(
        [[3, 0], [0, 0], [0, -2]]
    )  # ? this the matrix that form the transformation in row 752
    print("Transformation matrix:\n", A, "\n")
    w = A @ v
    return w
# v = np.array([[3], [5]])
# w = L(v)
# print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)
"""
Every linear transformation can be carried out by matrix multiplication.
And vice versa, carrying out matrix multiplication, it is natural to consider the linear transformation that it represents.
It means you can associate the matrix with the linear transformation in some way.
This is a key connection between linear transformations and matrix algebra.
"""
# ============
#!# 4- Applications: Computer Graphics
# img = cv2.imread("./img.png", cv2.IMREAD_COLOR)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# image_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# plt.imshow(image_rotated)
# plt.show()
# ============########===============#################==================########################==============
# ============########===============#################==================########################==============
#!## Assignment 2
# grade-up-to-here
