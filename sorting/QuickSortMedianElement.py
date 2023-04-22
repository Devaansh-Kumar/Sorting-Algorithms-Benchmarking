def get_median(arr, low, high):
    mid = (low + high) // 2
    if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
        return mid
    elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
        return low
    else:
        return high


def partition(arr, low, high):
    pivot_index = get_median(arr, low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]

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


def quick_sort_with_pivot_as_median_element(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_with_pivot_as_median_element(arr, low, pi - 1)
        quick_sort_with_pivot_as_median_element(arr, pi + 1, high)