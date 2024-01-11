#defining graph vertices and edges
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E','C', 'A']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)

#adjacency matrix
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

for key in matrix_elements:
    for neighbour in graph.get(key):
        edges_list.append((key, neighbour))


#printing the edges list
print(edges_list)


#Now filling the adjacency matrix
for edge in edges_list:
    node1 = matrix_elements.index(edge[0])
    node2 = matrix_elements.index(edge[1])
    adjacency_matrix[node1][node2] = 1

#print adjacency matrix
print(adjacency_matrix)