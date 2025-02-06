# Challenge -- Convert an Incidence Matrix to a NetworkX Graph
# 
# Write a program that converts an indcidence matrix into a NetworkX graph object, then draw the graph
# Bonus: First verify that the matrix is a legitimate incidence matrix first!
# Bonus: Write a program that converts a NetworkX graph object into an incidence matrix

# Import the NetworkX package for creating graphs, matplotlib.pyplot for plotting them
import networkx as nx
import matplotlib.pyplot as plt


# Hard-coded Incidence matrix. Play around and make changes to test your program.
M = [[1,-1,0,0,0],[1,0,-1,0,0],[1,0,0,-1,0],[0,1,-1,0,0],[0,1,0,-1,0], [0,1,0,0,-1],[0,0,1,-1,0]]

example_row_1 = [0,0,0,0,0,1,0,0,-1]
example_row_2 = [0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

# A helpful piece of code:
# The index method return the index number of a element of a list

print(example_row_1,example_row_1.index(1))
print(example_row_2,example_row_2.index(-1))

e = (example_row_1.index(1),example_row_2.index(-1))

print(e)


# builds a graph from an incidence matrix
def buildGraph(M):
    # checks if it's an incidence matrix
    for i in range(len(M[0])):
       total = 0
       for j in range(len(M)):
            total += abs(M[j][i])
       if total != 2:
           return "not an incidence matrix!"
    # adds the edges
    G = nx.Graph()
    for edge in M:
        G.add_edge(edge.index(1), edge.index(-1))
    return G

graph1 = buildGraph(M)
# nx.draw_networkx(graph1)
plt.show()

# builds an incidence matrix from a graph
def buildMatrix(G):
    edges = G.edges()
    numNodes = max(map(max, edges))
    print("haha" + str(numNodes))
    M = [] * len(edges)
    for edge in edges:
        row = [0] * (numNodes + 1)
        row[edge[0]] = 1
        print(str(edge[0]) + " " + str(edge[1]))
        row[edge[1]] = -1
        M.append(row)
    return M
matrix1 = buildMatrix(graph1)
print(matrix1)