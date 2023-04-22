from sorting import HeapSort, InsertionSort, MergeSort, RadixSort, QuickSortFirstElement, QuickSortMedianElement, QuickSortRandomElement
import os
import time
import pandas as pd
import matplotlib.pyplot as plt

# t = [34,34,35,3,4234,24,3,4]

def loader(path) -> list:
    with open(path,'r') as f:
        l = f.readlines()
        t = [int(i) for i in l[1::]]

        return t

def timing_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function {func.__name__!r} executed in {end_time - start_time:.5f} seconds")
        time_taken = end_time - start_time
        return (result,time_taken)
    return wrapper

def evaluate_sort(sort_func):
    wrapped_func = timing_function(sort_func)

    times = dict() #dict of lists for each directory, storing a tuple of size and time that is taken

    directories = ["random", "increasing", "decreasing"]

    for directory in directories:
        file_names = os.listdir("./"+directory)

        times[directory] = []

        for file in file_names:
            list_of_numbers = loader("./"+directory+"/"+file)

            _ , time_taken = wrapped_func(list_of_numbers)

            print(f"Time taken for {directory} numbers of {file} to be sorted is {time_taken}")

            times[directory].append((len(list_of_numbers),time_taken))

        times[directory] = sorted(times[directory])

    return times

def visualise_images(times,sorting_algorithm: str):
    #Get times directly from evaluate_sort
    df = pd.DataFrame(times)
    df['sizes'] = [i[0] for i in df['random'].values]
    df['random'] = [i[1] for i in df['random'].values]
    df['increasing'] = [i[1] for i in df['increasing'].values]
    df['decreasing'] = [i[1] for i in df['decreasing'].values]

    plt.title()

def g_img(times, func):

    df = pd.DataFrame(times)
    df['sizes'] = [i[0] for i in df['random'].values]
    df['random'] = [i[1] for i in df['random'].values]
    df['increasing'] = [i[1] for i in df['increasing'].values]
    df['decreasing'] = [i[1] for i in df['decreasing'].values]

    title = " ".join(func.__name__.split('_')).title()
    image_name = func.__name__

    plt.title(f"Sorting using {title}")
    plt.plot(df['sizes'],df['random'],marker='o',label='random')
    plt.plot(df['sizes'],df['increasing'],marker='o',label='increasing')
    plt.plot(df['sizes'],df['decreasing'],marker='o',label='decreasing')
    plt.legend()
    plt.rcParams['figure.figsize'] = [10,10]
    plt.xlabel('size')
    plt.ylabel('times (s)')
    plt.savefig(image_name + "linear" + ".png")
    plt.yscale('log')
    plt.savefig(image_name + "log" + ".png")

sorting = [HeapSort.heap_sort, InsertionSort.insertion_sort, MergeSort.merge_sort, RadixSort.radix_sort, QuickSortFirstElement.quick_sort_with_pivot_as_first_element, QuickSortRandomElement.quick_sort_with_pivot_as_random_element, QuickSortMedianElement.quick_sort_with_pivot_as_median_element]

for algorithm in sorting:
    temp_times = evaluate_sort(algorithm)
    g_img(temp_times, algorithm)

