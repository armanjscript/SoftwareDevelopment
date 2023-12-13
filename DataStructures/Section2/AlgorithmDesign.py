#linear search (Complexity(n))

def linear_search(input_list, element):

    for index, value in enumerate(input_list):
        if value == element:
            return index
    return -1

input_list = [3, 9, 2, 6, 7, 1, 8]
element = 7

print('index position for element:', linear_search(input_list, element))