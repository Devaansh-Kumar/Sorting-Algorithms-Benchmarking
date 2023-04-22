def partition(array, low, high):
   
    # First Element as pivot
    pivot = array[low]
     
    # st points to the starting of array
    start = low + 1
     
    # end points to the ending of the array
    end = high
 
    while True:
        # It indicates we have already moved all the elements to their correct side of the pivot
        while start <= end and array[end] >= pivot:
            end = end - 1
 
        # Opposite process
        while start <= end and array[start] <= pivot:
            start = start + 1
 
        # Case in which we will exit the loop
        if start <= end:
            array[start], array[end] = array[end], array[start]
            # The loop continues
        else:
            # We exit out of the loop
            break
 
    array[low], array[end] = array[end], array[low]
    return end

def quick_sort_with_pivot_as_first_element(array, low, high):
    if low < high:
        idx = partition(array, low, high)
        quick_sort_with_pivot_as_first_element(array, low, idx-1)
        quick_sort_with_pivot_as_first_element(array, idx+1, high)