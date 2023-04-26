import random

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort_with_pivot_as_random_element(arr, low, high):
    if low < high:
        # Selecting a random pivot
        random_pivot_index = random.randint(low, high)
        arr[low], arr[random_pivot_index] = arr[random_pivot_index], arr[low]

        pi = partition(arr, low, high)
        quick_sort_with_pivot_as_random_element(arr, low, pi - 1)
        quick_sort_with_pivot_as_random_element(arr, pi + 1, high)

