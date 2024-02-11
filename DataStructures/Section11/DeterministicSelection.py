def partition(unsorted_array, first_index, last_index): 
    if first_index == last_index: 
        return first_index 
    else: 
        nearest_median = median_of_medians(unsorted_array[first_index:last_index]) 
    index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median) 
    swap(unsorted_array, first_index, index_of_nearest_median) 
 
    pivot = unsorted_array[first_index] 
    pivot_index = first_index

    index_of_last_element = last_index 
    less_than_pivot_index = index_of_last_element 
    greater_than_pivot_index = first_index + 1 
 
    ## This while loop is used to correctly place pivot element at its correct position 
    while 1:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1
 
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break
 
    unsorted_array[pivot_index]=unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index]=pivot
    return less_than_pivot_index

def median_of_medians(elems):  
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)] 
    medians = [] 
    for sublist in sublists: 
        medians.append(sorted(sublist)[int(len(sublist)/2)]) 
    if len(medians) <= 5: 
        return sorted(medians)[int(len(medians)/2)]
    else:
        return median_of_medians(medians)

def get_index_of_nearest_median(array_list, first, last, median): 
    if first == last: 
        return first 
    else: 
        return array_list.index(median)

def swap(array_list, first, index_of_nearest_median):
    temp = array_list[first]
    array_list[first] = array_list[index_of_nearest_median]
    array_list[index_of_nearest_median] = temp


def deterministic_selection(array_list, start, end, k): 
    split = partition(array_list, start, end) 
    if split == k: 
        return array_list[split] 
    elif split < k:
        return deterministic_selection(array_list, split + 1, end, k) 
    else: 
        return deterministic_selection(array_list, start, split-1, k)


#Output of deterministic selection
list1= [2, 3, 5, 4, 1, 12, 11, 13, 16, 7, 8, 6, 10, 9, 17, 15, 19, 20, 18, 23, 21, 22, 25, 24, 14]
print("The 6th smallest element is", deterministic_selection(list1, 0, len(list1)-1, 5))