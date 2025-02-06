# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/16/23

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix
3
row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]


# print("Here is matrix M shown as a table in Python:\n")
# print(tabulate(M))


# Create a new copy of the matrix
# deepcopy creates a copy of values, not a copy of references
N = copy.deepcopy(M)

# Ask user to perform an elementary row operation
# row_choice = input("Choose a row to multiply by a scalar:  ")
# scalar = input("Enter a scalar to multiply by:  ")

# # Convert row_choice to the appropriate index for the list
# # Remember: Python uses 0-indexing
# row = int(row_choice) - 1
# # Convert the string input to a float
# scalar = float(scalar)

# # Perform the elementary row operation
# # Note: There are more Python-like ways to do this, but this approach emphasizes the matrix structure of the list of lists

# for i in range(len(N[row])):
#   N[row][i]=scalar*N[row][i]

# print("Here is the new matrix:")
# print(tabulate(N))



# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")

###################### EASY ########################
# return a row selected by the user
def get_row(M, row):
  return M[row-1]

# return a column selected by the user
def get_col(M, col):
  column = []
  for i in range(len(M)):
    column.append(M[i][col-1])
  return column

# allow the user to specify an entry to change and allow them to change it
def change_entry(M, row, col, new):
  M[row-1][col-1] = new
  return M
# change_entry(N, 3, 4, 100)
# print(tabulate(N))

# implement the other elementary row operations on the hard-coded matrix
def swap(M, row1, row2):
  temprow = M[row1-1]
  M[row1-1] = M[row2-1]
  M[row2-1] = temprow
# swap(N, 3, 2)
# print(tabulate(N))

def add_scalar_multiple(M, row1, row2, scalar):
  ''' row 1 is being changed '''
  for i in range(len(M[row1-1])):
    M[row1-1][i] += int(M[row2-1][i]) * float(scalar)

# add_scalar_multiple(N, 2, 3, 2)
# print(tabulate(N))


###################### MED ########################
# Write a program that allows the user to enter a custom matrix
def create_matrix():
  ''' creates a matrix based on input '''
  inputStr = input("Input a matrix, with spaces separating entries on the same row and commas separating rows: ")
  M = []
  row = []
  inputL = inputStr.split()
  for i in inputL:
    # print(i)
    if i == " ":
      continue
    elif "," in i:
      row.append(i[:-1])
      M.append(row)
      row = []
    else:
      row.append(i)
  M.append(row)
  print("The matrix is: \n" + tabulate(M))
  return M

# newM = create_matrix()

# Implement all three elementary row operations and let the user to choose which one to perform
## -- see above for swap() and add_scalar_multiple()

def scalar_multiple(M, row, scalar):
  for i in range(len(M[row-1])):
    M[row-1][i] = int(M[row-1][i]) * scalar
  return M

# scalar_multiple(newM, 2, 2)
# print(tabulate(newM))

def choose():
  inp = input("Choose from the following elementary operations: swap rows, multiply a row by a scalar, add a scalar multiple to a row. Input 1 2 or 3")
  if inp == "1":
    rows = input("Which two rows? ")
    rowsL = rows.split()
    swap(newM, int(rowsL[0]), int(rowsL[1]))
  elif inp == "2":
    row = input("Which row, and what scalar? ")
    rowL = row.split()
    scalar_multiple(newM, int(rowL[0]), int(rowL[1]))
  elif inp == "3":
    info = input("Add a scalar multiple of x of y row to z row. Enter x y z: ")
    info = info.split()
    add_scalar_multiple(newM, int(info[2]), int(info[1]), int(info[0]))
  else:
    print("invalid response")
  print(tabulate(newM))


# choose()

###################### HARD ########################
# Write a program that puts the hard-coded matrix into reduced row echelon form

newM = [[1, 2, 3, 4, 5], [6, 7, 78, 23, 5], [2, 5, 23, 32, 5], [2, 5, 33, 23, 5]]

#pivot is index based
def rref(M, pivot):
    if pivot > (len(M[0]) - 2):
      print("yay" + str(pivot))
      print(tabulate(M))
      return
    
    print("starting: \n" + tabulate(M) + "\npivot: " + str(pivot) + "\n")

    if int(M[pivot][pivot]) != 1:
        # print(int(M[i][pivot]))
        # print(i)
        # print("i: " + str(i) + "  pivot: " + str(pivot))
        scalar_multiple(M, pivot+1, (1/float(M[pivot][pivot])))
        print("scale to be 1: \n" + tabulate(M))

    # print(tabulate(M))
    for i in range(len(M)):
        if M[i][pivot] != 0 and i != pivot:
            scalar = -1 * M[i][pivot]
            add_scalar_multiple(M, i+1, pivot+1, scalar)
            print("a new 0 should appear: \n" + tabulate(M))
    
    rref(M, pivot+1)

rref(newM, 0)

# M - pivot = row?