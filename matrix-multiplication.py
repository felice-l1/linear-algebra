# Intro to Matrix Multiplication
# A starter for exploring matrix multiplication

# Import the csv module for handling data
import csv

# Makes presenting a table of data easier
from tabulate import tabulate

# The matrix M is encoded as a list of lists
# Recall that the nested lists serve as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]

# We'll import the matrix N from a file using the CSV library
# Recall: This reads in the comma separated-values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  N = list(reader)

# By default lists have strings as entries, so convert them to floats
for i in range(len(N)):
  for j in range(len (N[i])):
    N[i][j]=float(N[i][j])
    

print(tabulate(M))
print("\n")
print(tabulate(N))
print("\n")


# Challenge 1
# Write a function that returns the dimensions of a matrix

# Returns the dimensions of matrix A as a tuple (number of rows, number of columns)
def matrix_dimensions(A):
  num_rows = len(A)
  num_cols = len(A[0])
  return((num_rows,num_cols))

print(matrix_dimensions(M))
print(matrix_dimensions(N))

# Challenge 2
# Write a function that determines if two matrices can be multiplied

# Returns True or False
def can_multiply_matrices(A,B):
  Adimension = matrix_dimensions(A)
  Bdimension = matrix_dimensions(B)
  if (Adimension[1]==Bdimension[0]):
    return True
  else:
    return False
print(can_multiply_matrices(M,N))
print(can_multiply_matrices(N,M))


# Challenge 3
# Write a function that determines the entry in row i, column j of the matrix product A*B 

# Returns the entry in row i, column j of the matrix product A*B

def matrix_product_entry(A,B,i,j):
    if not can_multiply_matrices(A,B):
      return False
    total = 0
    column = []
    for k in range(len(B)):
      column.append(B[k][j])
    for l in range(len(column)):
      total += A[i][l] * column[l]
    return total

print(matrix_product_entry(N,M,0,0))
print(matrix_product_entry(N,M,0,1))



# Challenge 4
# Write a function that multiplies two matrices A and B

# Returns the matrix product

def matrix_product(A,B):
  if not can_multiply_matrices(A,B): return False
  dimensions = (matrix_dimensions(A)[0], matrix_dimensions(B)[1])
  finalMatrix = []
  for row in range(dimensions[0]):
    currRow = []
    for col in range(dimensions[1]):
      currRow.append(matrix_product_entry(A,B,row,col))
    finalMatrix.append(currRow)
  return finalMatrix

  # Should probably check first to see if the matrices can be multiplied!

print(tabulate(matrix_product(N,M)))

# Challenge 5
# Write a function that transposes a matrix
  
def matrix_transpose(A):
  M = []
  print(M)
  for c in range(len(A[0])):
    Mrow =[]
    for r in range(len(A)):
      Mrow.append(A[r][c])
    M.append(Mrow)
  return M

print(tabulate(matrix_transpose(N)))
print(tabulate(matrix_transpose(M)))

  