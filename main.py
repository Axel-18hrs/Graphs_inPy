import networkx as nx

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4, 5])

G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)])

# check if there is an edge between two vertices
has_edge = G.has_edge(1, 2)

# Iterate through nodes and edges
print("Nodes:")
for node in G.nodes():
    print(f"Node: {node}")

print("\nEdges:")
for edge in G.edges():
    print(f"Edge: {edge[0]} -> {edge[1]}")

# Calculate the degree of a node
node_degree = G.degree(1)
print("\nDegree of node 1:", node_degree)

# Find the neighbors of a node
neighbors = list(G.neighbors(3))
print("\nNeighbors of node 3:", neighbors)
