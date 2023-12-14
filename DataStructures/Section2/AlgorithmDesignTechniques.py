# factorial (Recursive)

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))


# divide and conquer (Binary Search)

def binary_search(arr, start:int, end:int, key):
    while start <= end:
        mid = start + (end - start)/2
        mid = int(mid)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


arr = [4, 6, 9, 13, 14, 18, 21, 24, 38] 
x = 9
result = binary_search(arr, 0, len(arr)-1, x)  
print(result)

# merge sort 

def merge_sort(unsorted_list):

    if len(unsorted_list) == 1:
        return unsorted_list
    mid_point = int(len(unsorted_list)/2)
    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)
    return merge(half_a,half_b)

def merge(first_sublist, second_sublist):
    i = j =0
    merged_list = []

    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist [j]:
            merged_list.append(first_sublist[i])
            i = i + 1
        else:
            merged_list.append(second_sublist[j])
            j = j + 1
    while i < len(first_sublist):
            merged_list.append(first_sublist[i])
            i = i + 1
    while j < len(second_sublist):
            merged_list.append(second_sublist[j])
            j = j + 1
    return merged_list

a= [11, 12, 7, 41, 61, 13, 16, 14] 
print(merge_sort(a))

#recursive solution for fibonacci

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(5):
    print(fib(i))

#dynamic programming solution for fibonacci

def dyn_fib(n):

    if n==0:
        return 0
    if n==1:
        return 1
    
    if lookup[n] is not None:
        return lookup[n]
    
    lookup[n] = dyn_fib(n-1) + dyn_fib(n-2)
    return lookup[n]

lookup = [None] * 1000

for i in range(6):
    print(dyn_fib(i))


# greedy algorithm dijkstra

print('===========================')

graph = dict() 
graph['A'] = {'B': 5, 'D': 9, 'E': 2} 
graph['B'] = {'A': 5, 'C': 2}
graph['C'] = {'B': 2, 'D': 3} 
graph['D'] = {'A': 9, 'F': 2, 'C': 3} 
graph['E'] = {'A': 2, 'F': 3} 
graph['F'] = {'E': 3, 'D': 2}

table = { 
    'A': [0, None], 
    'B': [float("inf"), None], 
    'C': [float("inf"), None], 
    'D': [float("inf"), None], 
    'E': [float("inf"), None], 
    'F': [float("inf"), None], 
}

DISTANCE = 0
PREVIOUS_NODE = 1

INFINITY = float('inf')

def get_shortest_distance(table, vertex):
    shortest_distabnce = table[vertex][DISTANCE]
    return shortest_distabnce

def set_shortest_distance(table, vertex, new_distance):
    table[vertex][DISTANCE] = new_distance

def set_previous_node(table, vertex, previous_node):
    table[vertex][PREVIOUS_NODE] = previous_node

def get_distance(graph, first_vertex, second_vertex):
    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_nodes):
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
    assumed_min = table[unvisited_nodes[0]][DISTANCE]
    min_vertex = unvisited_nodes[0]

    for node in unvisited_nodes:
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_vertex = node

def find_shortest_path(graph, table, origin):
    visited_nodes = []
    current_node = origin
    starting_node = origin
    
    while True:
        adjacent_nodes = graph[current_node]
        if set(adjacent_nodes).issubset(set(visited_nodes)):
            pass
        else:
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes))
        
        for vertex in unvisited_nodes:
            distance_from_starting_node = get_shortest_distance(table, vertex)
            if distance_from_starting_node == INFINITY and current_node == starting_node:
                total_distance = get_distance(graph, vertex, current_node)
            else:
                total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex)
            if total_distance < distance_from_starting_node:
                set_shortest_distance(table, vertex, total_distance)
                set_previous_node(table, vertex, current_node)
        visited_nodes.append(current_node)
        if len(visited_nodes) == len(table.keys()):
            break
        current_node = get_next_node(table, visited_nodes)
    return table


shortest_distance_table = find_shortest_path(graph, table, 'A') 
for k in sorted(shortest_distance_table): 
     print("{} - {}".format(k,shortest_distance_table[k]))