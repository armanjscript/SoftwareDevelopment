#Buuble Sort

def bubble_sort(unordered_list):
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number, 0, -1):
        for j in range(i):
            if unordered_list [j] > unordered_list[j + 1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j + 1]
                unordered_list[j + 1] = temp


print("-----Bubble Sort Outputs-----\n")
my_list = [4,3,2,1]
bubble_sort(my_list)
print(my_list, '\n')

my_list = [1,12,3,4]
bubble_sort(my_list)
print(my_list)


