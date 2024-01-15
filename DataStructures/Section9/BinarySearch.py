def binary_search_iterative(ordered_list, term):
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2

        if ordered_list[mid_point] == term:
            return mid_point
        if ordered_list[mid_point] > term:
            index_of_last_element = mid_point - 1
        else:
            index_of_first_element = mid_point + 1
    if index_of_first_element > index_of_last_element:
        return None


print("---First Output---\n")
list1 = [10, 30, 100, 120, 500]
 
search_term = 10
index_position1 = binary_search_iterative(list1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term, index_position1))
    
print("---Second Output---\n")

list2 = ['book','data','packt', 'structure']
 
search_term2 = 'structure'
index_position2 = binary_search_iterative(list2, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))



print('---Binary Search Recursive---\n')
#Recursive Binary Search
def binary_search_recursive(ordered_list, first_element_index, last_element_index, term):
    if last_element_index < first_element_index:
        return None 
    else:
        mid_point = (first_element_index + last_element_index) // 2
        if ordered_list[mid_point] > term:
            return binary_search_recursive(ordered_list, first_element_index, mid_point - 1, term)
        elif ordered_list[mid_point] < term:
            return binary_search_recursive(ordered_list, mid_point + 1, last_element_index, term)
        else:
            return mid_point

print("Binary Search Recursive output1--\n")
list1 = [10, 30, 100, 120, 500]
 
search_term = 10
index_position1 =  binary_search_recursive(list1, 0, len(list1)-1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term, index_position1))

print('\n')

print("Binary Search Recursive output2--\n")
list2 = ['book','data','packt',  'structure']
 
search_term2 = 'data'
index_position2 = binary_search_recursive(list2, 0, len(list1)-1, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))