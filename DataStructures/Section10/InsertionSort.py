#Insertion Sort

def insertion_sort(unsorted_list):
    for i in  range(1, len(unsorted_list)):
        search_index = i
        insert_value = unsorted_list[i]
        while search_index > 0 and unsorted_list[search_index - 1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index - 1]
            search_index -= 1
        unsorted_list[search_index] = insert_value


print("-----Insertion Sort Outputs-----\n")
my_list = [5, 1, 100, 2, 10]
print("Original list", my_list)
insertion_sort(my_list)
print("Sorted list", my_list) 