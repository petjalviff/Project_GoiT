from typing import List

def quick_select(arr: List[int], k: int) -> int:
#  Функція пошуку k-го найменшого елемента за допомогою Quick Select
    if not (1 <= k <= len(arr)):
        raise ValueError("k shoud be from 1 to array length")

    def partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quick_select_helper(low: int, high: int, k_smallest: int) -> int:
        if low == high:
            return arr[low]

        pivot_index = partition(low, high)

        if k_smallest == pivot_index:
            return arr[pivot_index]
        elif k_smallest < pivot_index:
            return quick_select_helper(low, pivot_index - 1, k_smallest)
        else:
            return quick_select_helper(pivot_index + 1, high, k_smallest)

    return quick_select_helper(0, len(arr) - 1, k - 1)


# Приклад використання
array = [3, 11, 41, 17, 52, 2, 82, 36, 45, 13, 85]
k = 4
result = quick_select(array, k)
print(f"{k}-й найменший елемент: {result}")