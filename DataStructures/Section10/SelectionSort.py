def selection_sort(unordered_list):
    size_of_list = len(unordered_list) - 1
    for i in range(size_of_list):
        small = i
        for  j in range(i+1, size_of_list):
            if unordered_list[j] < unordered_list[small]:
                small = j
        temp = unordered_list[i]
        unordered_list[i] = unordered_list[small]
        unordered_list[small] = temp


a_list = [3, 2, 35, 4, 32, 94, 5, 7]
print("List before sorting", a_list)
selection_sort(a_list)
print("List after sorting", a_list)