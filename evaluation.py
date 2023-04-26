from sorting import HeapSort, InsertionSort, MergeSort, RadixSort, QuickSortFirstElement, QuickSortMedianElement, QuickSortRandomElement
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10000000)
TRIALS = 1
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
        print(f"Function {func.__name__!r} executed in {end_time - start_time} seconds")
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

            print(f"Sorting {len(list_of_numbers)} numbers")
            
            total_time_taken = 0

            for _ in range(TRIALS):

                if sort_func not in [QuickSortFirstElement.quick_sort_with_pivot_as_first_element, QuickSortRandomElement.quick_sort_with_pivot_as_random_element, QuickSortMedianElement.quick_sort_with_pivot_as_median_element]:
                    _ , time_taken = wrapped_func(list_of_numbers)

                else:
                    _ , time_taken = wrapped_func(list_of_numbers,low=0,high=len(list_of_numbers)-1)
                
                total_time_taken += time_taken

            avg_time_taken = total_time_taken/TRIALS

            print(f"Time taken for {directory} numbers of {file} to be sorted is {avg_time_taken} seconds\n")

            times[directory].append((len(list_of_numbers),avg_time_taken))

        times[directory] = sorted(times[directory])

    return times

def put_in_folder(path):
    return "plots/"+path

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
    image_name = "plots/"+func.__name__

    plt.title(f"Sorting using {title}")
    plt.plot(df['sizes'],df['random'],marker='o',label='random')
    plt.plot(df['sizes'],df['increasing'],marker='o',label='increasing')
    plt.plot(df['sizes'],df['decreasing'],marker='o',label='decreasing')
    plt.legend()
    plt.rcParams['figure.figsize'] = [10,10]
    plt.xlabel('Sizes')
    plt.ylabel('Times (s)')
    plt.savefig(image_name + "_linear" + ".png")
    plt.yscale('log')
    plt.savefig(image_name + "_log" + ".png")
    plt.clf()


def quick_img():
    temp_times_first = evaluate_sort(QuickSortFirstElement.quick_sort_with_pivot_as_first_element)
    temp_times_median = evaluate_sort(QuickSortMedianElement.quick_sort_with_pivot_as_median_element)
    temp_times_random = evaluate_sort(QuickSortRandomElement.quick_sort_with_pivot_as_random_element)


    def gen_df(times):
        df = pd.DataFrame(times)
        df['sizes'] = [i[0] for i in df['random'].values]
        df['random'] = [i[1] for i in df['random'].values]
        df['increasing'] = [i[1] for i in df['increasing'].values]
        df['decreasing'] = [i[1] for i in df['decreasing'].values]
        return df

    df_first = gen_df(temp_times_first)
    df_median = gen_df(temp_times_median)
    df_random = gen_df(temp_times_random)

    def fig_plot_save(title,image_name):
        plt.title(f"Sorting using {title}")
        plt.legend()
        plt.rcParams['figure.figsize'] = [10,10]
        plt.xlabel('Sizes')
        plt.ylabel('Times (s)')
        plt.savefig(image_name + "_linear" + ".png")
        plt.yscale('log')
        plt.savefig(image_name + "_log" + ".png")

        plt.clf()

    #This is for the best case

    title = "Best case for all the three Quicksorts"
    image_name = "plots/"+"best_case_all_quick"

    plt.plot(df_first['sizes'],df_first['random'],marker='o',label='First element')
    plt.plot(df_median['sizes'],df_median['increasing'],marker='o',label='Median element')
    plt.plot(df_random['sizes'],df_random['increasing'],marker='o',label='Random element')


    fig_plot_save(title,image_name)

    #This is for the worst case

    title = "Worst case for all the three Quicksorts"
    image_name = "plots/"+"worst_case_all_quick"

    plt.plot(df_first['sizes'],df_first['decreasing'],marker='o',label='First element')
    plt.plot(df_median['sizes'],df_median['decreasing'],marker='o',label='Median element')
    plt.plot(df_random['sizes'],df_random['random'],marker='o',label='Random element')

    fig_plot_save(title,image_name)

    #This is for the average case

    title = "Average case for all the three Quicksorts"
    image_name = "plots/"+"average_case_all_quick"

    plt.plot(df_first['sizes'],df_first['random'],marker='o',label='First element')
    plt.plot(df_median['sizes'],df_median['random'],marker='o',label='Median element')
    plt.plot(df_random['sizes'],df_random['random'],marker='o',label='Random element')

    fig_plot_save(title,image_name)

def compare_all_sort_img():
    temp_times_insertion = evaluate_sort(InsertionSort.insertion_sort)
    temp_times_merge = evaluate_sort(MergeSort.merge_sort)
    temp_times_quick = evaluate_sort(QuickSortRandomElement.quick_sort_with_pivot_as_random_element)
    temp_times_heap = evaluate_sort(HeapSort.heap_sort)
    temp_times_radix = evaluate_sort(RadixSort.radix_sort)

    def gen_df(times):
        df = pd.DataFrame(times)
        df['sizes'] = [i[0] for i in df['random'].values]
        df['random'] = [i[1] for i in df['random'].values]
        df['increasing'] = [i[1] for i in df['increasing'].values]
        df['decreasing'] = [i[1] for i in df['decreasing'].values]
        return df

    df_insertion = gen_df(temp_times_insertion)
    df_merge = gen_df(temp_times_merge)
    df_quick = gen_df(temp_times_quick)
    df_heap = gen_df(temp_times_heap)
    df_radix = gen_df(temp_times_radix)

    def fig_plot_save(title,image_name):
        plt.title(f"Sorting using {title}")
        plt.legend()
        plt.rcParams['figure.figsize'] = [10,10]
        plt.xlabel('Size')
        plt.ylabel('Times (s)')
        plt.savefig(image_name + "_linear" + ".png")
        plt.yscale('log')
        plt.savefig(image_name + "_log" + ".png")

        plt.clf()

    #This is for the best case

    title = "Best case for all the Sorting Algorithms"
    image_name = "plots/"+"all_sort_best_case"

    plt.plot(df_insertion['sizes'],df_insertion['increasing'],marker='o',label='insertion')
    plt.plot(df_merge['sizes'],df_merge['random'],marker='o',label='merge')
    plt.plot(df_quick['sizes'],df_quick['random'],marker='o',label='quick')
    plt.plot(df_heap['sizes'],df_heap['random'],marker='o',label='heap')
    plt.plot(df_radix['sizes'],df_radix['random'],marker='o',label='radix')


    fig_plot_save(title,image_name)

    #This is for the worst case

    title = "Worst case for all the Sorting Algorithms"
    image_name = "plots/"+"all_sort_worst_case"

    plt.plot(df_insertion['sizes'],df_insertion['decreasing'],marker='o',label='insertion')
    plt.plot(df_merge['sizes'],df_merge['random'],marker='o',label='merge')
    plt.plot(df_quick['sizes'],df_quick['random'],marker='o',label='quick')
    plt.plot(df_heap['sizes'],df_heap['random'],marker='o',label='heap')
    plt.plot(df_radix['sizes'],df_radix['random'],marker='o',label='radix')

    fig_plot_save(title,image_name)

    #This is for the average case

    title = "Average case for all the Sorting Algorithms"
    image_name = "plots/"+"all_sort_average_case"

    plt.plot(df_insertion['sizes'],df_insertion['random'],marker='o',label='insertion')
    plt.plot(df_merge['sizes'],df_merge['random'],marker='o',label='merge')
    plt.plot(df_quick['sizes'],df_quick['random'],marker='o',label='quick')
    plt.plot(df_heap['sizes'],df_heap['random'],marker='o',label='heap')
    plt.plot(df_radix['sizes'],df_radix['random'],marker='o',label='radix')

    fig_plot_save(title,image_name)


sorting = [QuickSortFirstElement.quick_sort_with_pivot_as_first_element, QuickSortMedianElement.quick_sort_with_pivot_as_median_element, QuickSortRandomElement.quick_sort_with_pivot_as_random_element, HeapSort.heap_sort, MergeSort.merge_sort, RadixSort.radix_sort, InsertionSort.insertion_sort]


def evaluate():
    for algorithm in sorting:
        temp_times = evaluate_sort(algorithm)
        g_img(temp_times, algorithm)

    quick_img()
    compare_all_sort_img()
