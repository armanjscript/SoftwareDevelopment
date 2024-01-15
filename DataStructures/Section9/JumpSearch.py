import math

def search_ordered(ordered_list, term):

    for i, item in enumerate(ordered_list):
        if item == term:
            return i
        elif item > term:
            return -1
    return -1


def jump_search(ordered_list, item):

    list_size = len(ordered_list)
    block_size = int(math.sqrt(list_size))
    i = 0

    while i != len(ordered_list) - 1 and ordered_list[i] <= item:
        if i + block_size > len(ordered_list):
            block_size = len(ordered_list) - i
            block_list = ordered_list[i:i+block_size]
            j = search_ordered(block_list, item)
            if j == -1:
                print('Element not found')
                return
        elif ordered_list[i + block_size] == item:
            return i+blocksize-1
        elif ordered_list [i + block_size] > item:
            block_array = ordered_list[i : i+ block_size - 1]
            j = search_ordered(block_array, item)
            if j == -1:
                print("Element not found")
                return 
            return i + j
        i += block_size

print(jump_search([1,2,3,4,5,6,7,8,9, 10, 11], 8))