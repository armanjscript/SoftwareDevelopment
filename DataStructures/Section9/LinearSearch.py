#Linear Search on unsorted list
def search(unsorted_list, term):
    for i, item in enumerate(unsorted_list):
        if item == term:
            return i
    return None

print("----unsorted list----\n")

list1 = [60, 1, 88, 10, 11, 600]
search_term = 10
index_position = search(list1, search_term) 
print(index_position)
list2 = ['packt', 'publish', 'data']
search_term2 = 'data'
Index_position2 = search(list2, search_term2)
print(Index_position2)

#Linear Search on ordered list
def search_ordered(ordered_list, term):
    for i, item in enumerate(ordered_list):
        if item == term:
            return i
        elif item > term:
            return None
    return None

print('----ordered list----\n')

list1 = [2, 3, 4, 6, 7] 
search_term = 5
index_position1 = search_ordered(list1, search_term)
 
if index_position1 is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, index_position1))


list2 = ['book','data','packt', 'structure']
search_term2 = 'structure'
index_position2 = search_ordered(list2, search_term2)
if index_position2 is None:
    print("{} not found".format(search_term2))
else:
    print("{} found at position {}".format(search_term2, index_position2))