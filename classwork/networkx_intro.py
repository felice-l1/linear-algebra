# Graphs in Python
# A simple example of using the NetworkX package for creating graphs
# by Patrick Honner, 10/1/2022

# Lots more information here:
# https://networkx.org/documentation/stable/tutorial.html

# Also a nice introduction by mathematician Robert Talbert here:
# https://github.com/RobertTalbert/discretecs/blob/de1a7a42f576da375f2c2f809fdf75aa15b3a91a/Graphs_in_Python_with_networkX.ipynb


# Import the NetworkX package
import networkx as nx

# Import matplotlib.pyplot, a package for creating mathematical plots
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# An edge is an ordered pair of nodes.
# Add an edge by specifying a pair of nodes
G.add_edge(1,2)

# Add multiple edges from a list of ordered pairs
# G.add_edge(2, 3)
G.add_edges_from([(1,3), (2,4), (2,3), (1,5)])


# List the edges
for e in G.edges(): 
  print(e)

# List the nodes
for v in G.nodes(): 
  print(v)

# NetworkX's draw function, which requires matplotlib.pyplot

nx.draw_networkx(G, with_labels = True, node_color="lightblue")

# Need to tell pyplot to show the plot
plt.show()

#  See NetworkX tutorial (https://networkx.org/documentation/stable/tutorial.html) for more plotting options
# As well as matplotlib.pyplot tutorial (https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.html)

