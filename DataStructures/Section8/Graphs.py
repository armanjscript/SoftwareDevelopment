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

print("--------------->")

#Breadth First Search
graph = dict()
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']

from collections import deque

def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_deque = deque([root])
    visited_vertices.append(root)
    node = root
    while len(graph_deque) > 0:
        node = graph_deque.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_deque.append(elem)
    return visited_vertices


print(breadth_first_search(graph, 'A'))
