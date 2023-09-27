def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:  # Если элемент найден, возвращаем его индекс
            return mid
        elif arr[mid] < target:  # Если искомый элемент больше значения в середине, ищем в правой половине массива
            low = mid + 1
        else:  # Если искомый элемент меньше значения в середине, ищем в левой половине массива
            high = mid - 1

    return -1  # Искомый элемент не найден

# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)
print("Индекс элемента:", result)
