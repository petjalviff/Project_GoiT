from typing import List, Tuple


def find_min_max(arr: List[int]) -> Tuple[int, int]:
    # Функція пошуку максимального та мінімального елементів за допомогою "розділяй і володарюй"
    def divide_and_conquer(low: int, high: int) -> Tuple[int, int]:
        if low == high:
            return arr[low], arr[low]

        if high == low + 1:
            return (min(arr[low], arr[high]), max(arr[low], arr[high]))

        mid = (low + high) // 2
        left_min, left_max = divide_and_conquer(low, mid)
        right_min, right_max = divide_and_conquer(mid + 1, high)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        raise ValueError("Array can`t be empty")

    return divide_and_conquer(0, len(arr) - 1)

# Приклад використання
array = [3, 11, 41, 17, 52, 2, 82, 36, 45, 13, 85]
min_val, max_val = find_min_max(array)
print(f"Мінімум: {min_val}, Максимум: {max_val}")
