
# # *************************************** Quick sort - швидке сортування
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     print("pivot is", pivot)
#     left = [x for x in arr if x < pivot]
#     print("left is",left)
#     middle = [x for x in arr if x == pivot]
#     print("middle is",middle)
#     right = [x for x in arr if x > pivot]
#     print("right is",right)
#     print("*"*20)
#     return quicksort(left) + middle + quicksort(right)

# print(quicksort([8, 3, 2, 4, 5, 9, 6, 7, 1]))
# # Виведе: [2, 3, 4, 5, 8]

# n_arr=[8, 3, 2, 4, 5, 9, 6, 7, 1]
# left_list=[]
# for i in n_arr:
#     pivot_n=5
#     if i < pivot_n:
#         left_list.append(i)
# print(left_list)


