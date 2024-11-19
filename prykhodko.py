# This is for test
# Функція для бульбашкового сортування
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Порівнюємо сусідні елементи
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Міняємо місцями
    return arr

# Функція для сортування вибором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Шукаємо мінімальний елемент
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Міняємо місцями
    return arr

# Функція для сортування вставкою
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Елемент для вставки
        j = i - 1
        while j >= 0 and arr[j] > key:  # Переміщаємо більші елементи вправо
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Вставляємо елемент на правильну позицію
    return arr

# Приклад використання
if __name__ == "__main__":
    # Новий масив для сортування
    unsorted_data = [120, 55, 32, 78, 90, 101, 4, 61, 17, 44]  # Змінили масив

    # Виводимо результат кожного сортування
    print("Бульбашкове сортування:", bubble_sort(unsorted_data.copy()))
    print("Сортування вибором:", selection_sort(unsorted_data.copy()))
    print("Сортування вставкою:", insertion_sort(unsorted_data.copy()))
