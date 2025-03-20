import copy
import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tabulate import tabulate

from helper import build_graph
from helper import matrix_product
from helper import create_matrix

# some matrices to try: 
#    0 1 0 1, 1 0 1 1, 0 1 0 1, 1 1 1 0
#    0 1 1, 1 0 0, 1 0 0
#    0 1 0, 1 0 1, 0 1 0
initial_matrix = create_matrix()

# find out intial paths established in the matrix
# store the values in a dictionary, where the keys are nodes and the values are the nodes connected to that node
connections = {} 
for r in range(len(initial_matrix)):
   connections[r] = []
   for c in range(len(initial_matrix[r])):
      if initial_matrix[r][c] == 1:
         connections[r].append(c)

# establish the number of edges (aka the power the matrix is raised to)
num_edges = int(input("Enter the number of edges in the path: "))

# establish the start and end node, and stores that in the variables nodes
node_to_node = input("Enter the nodes that you want to track the paths between with a space between the two (nodes are numbered from 0): ")
nodes = [int(node_to_node[0]), int(node_to_node[-1])]

# gives us matrix ^ num_edges
final_matrix = initial_matrix
for i in range(num_edges-1):
   final_matrix = matrix_product(final_matrix, initial_matrix)

print("Matrix raised to the nth power, where n is the number of edges: ")
print(tabulate(final_matrix))

# initialize variable to hold all valid paths
all_paths = []

# updates all_paths to include all paths 
def find_paths(curr_path): 

    # if the number of moves is correct, and the last node is right
    if len(curr_path) == num_edges + 1 and curr_path[-1] == nodes[-1]:
      all_paths.append(curr_path)
    
    # base case: if the number of edges exceeds the established number, stop
    if len(curr_path) > num_edges:
       return
    
    # list is empty, start with the starting node
    if len(curr_path) == 0:
      curr_path.append(nodes[0])
    
    last_node = curr_path[-1]
    num_connections = len(connections[last_node])

    # make a copy of the current path for each possible next step
    copies = [copy.deepcopy(curr_path) for _ in range(num_connections)] 

    # for each possible next step, add that step and recursively call find_paths() again
    for i in range(num_connections):
       copies[i].append(connections[last_node][i])
       find_paths(copies[i])


# run find_paths so that all_paths contains all valid paths
find_paths([])

# check to see if the number of valid paths equals the corresponding entry in the matrix
print("Does the number of valid path equal the corresponding entry in the matrix?: " 
      + str((len(all_paths)) == final_matrix[nodes[0]][nodes[1]]))
print("Number of paths: " + str(len(all_paths)))

# prints all possible paths
print("All possible paths are: ")
for i in all_paths:
   print(i)




############## tried to animate edges turning different colors to show path; doesn't work ##############

# # creates given graph
# fig, ax = plt.subplots()
# G = build_graph(initial_matrix) 
# nx.draw_networkx(G, ax=ax)

# plt.show()

# colors = plt.get_cmap("plasma")

# pos = nx.spring_layout(G) # fix the node positions to prevent them from shifting around with each move

# print(type(colors))

# def update(frame):
#     print(frame)
#     # form edge tuples
#     edgelist = []
#     for i in range(2):
#        edgelist = (all_paths[0][i], all_paths[0][i+1])
#     #    print("hi")
#     #    print(edgelist)
#     #    print("bye")
#     #    print(edgelist[frame])
#        print(edgelist)
#        print("yeah")
#        nx.draw_networkx_edges(G, pos=pos, edgelist=[edgelist], edge_color=colors(random.uniform(0,1)), width=5)

# ani = animation.FuncAnimation(fig, update, frames=1, interval=1000, repeat = False) # frames = list of possible edges


# plt.show()
