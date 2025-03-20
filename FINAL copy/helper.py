import networkx as nx
from tabulate import tabulate

# creates a graph based on an adjacency matrix
def build_graph(M):
    # adds the edges
    G0 = nx.Graph()
    for i in range(len(M)):
        G0.add_edge(i, M[i].index(1))
    return G0

# checks if two matrices can be multiplied together
def can_multiply_matrices(A,B):
  A_cols = len(A[0]) # number of columns in A
  B_rows = len(B) # number of rows in B
  if A_cols == B_rows: 
    return True
  else:
    return False
  
# finds one entry of the resultant matrix in matrix multiplication
def matrix_product_entry(A,B,i,j):
    if not can_multiply_matrices(A,B): return False
    total = 0

    # extract the jth column in B
    column = []
    for k in range(len(B)):
      column.append(B[k][j])
    
    # dot product between the A's ith row and B's jth column
    for l in range(len(column)):
      total += A[i][l] * column[l]
    return total

# multiply two matrices
def matrix_product(A,B):
  if not can_multiply_matrices(A,B): return False
  dimensions = (len(A), len(B[0])) # dimension of the final matrix
  final_matrix = []
  for row in range(dimensions[0]):
    curr_row = []
    for col in range(dimensions[1]):
      curr_row.append(matrix_product_entry(A,B,row,col))
    final_matrix.append(curr_row)
  return final_matrix

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
      row.append(int(i[:-1]))
      M.append(row)
      row = []
    else:
      row.append(int(i))
  M.append(row)
  print("The matrix is: \n" + tabulate(M))
  return M