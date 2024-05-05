import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

test_list = [123, 5, 17, 256, 328, 8, 96, 111, 1, 555, 27, 224, 11, 76, 105]



# Вимірюємо час виконання insertion_sort
execution_time_insertion = timeit.timeit(lambda: insertion_sort(test_list.copy()), number=1000)
print("Час виконання сортування вставками insertion_sort:", execution_time_insertion)

# Вимірюємо час виконання merge_sort
execution_time_merge = timeit.timeit(lambda: merge_sort(test_list.copy()), number=1000)
print("Час виконання сортування злиттям merge_sort:", execution_time_merge)

# Вимірюємо час виконання sorted()
execution_time_sorted = timeit.timeit(lambda: sorted(test_list.copy()), number=1000)
print("Час виконання сортування вбудованним Timsort sorted():", execution_time_sorted)

if execution_time_insertion < execution_time_merge and execution_time_insertion < execution_time_sorted:
    print("сортування вставками insertion_sort виконуеться найшвидше з 3ьох методів")
elif execution_time_merge < execution_time_insertion and execution_time_merge < execution_time_sorted:
    print("сортування злиттям merge_sort виконуеться найшвидше з 3ьох методів")
else:
    print("сортування вбудованним Timsort sorted() виконуеться найшвидше з 3ьох методів")