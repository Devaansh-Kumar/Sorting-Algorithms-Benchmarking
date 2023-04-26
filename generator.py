import random
import os

def get_sizes(MAX_POWER_OF_10 : int = 4,FOLD_INCREASE : int = 3) -> list:
    """This function generates the different sizes of the input files.
        We will be taking the input sizes increasing by three-fold(default)

    Args:
        MAX_POWER_OF_10 (int): The maximum size of the dataset to be generated
        FOLD_INCREASE (int): The amount of exponential increase in the file

    Returns:
        list: of all the sizes of the dataset that are possible

    """
    sizes = []

    for i in range(1,MAX_POWER_OF_10+1):
        sizes.append(int(10**i/FOLD_INCREASE))
        sizes.append(10**i)

    for i in range(sizes[-2],sizes[-1],(10**(MAX_POWER_OF_10-1))*2):
        if i == sizes[-2]:
            continue
        sizes.append(i)

    return sorted(sizes)

def produce_file(FILE_SIZE : int) -> None:
    """This function will generate the dataset for a particular size with increasing, decreasing and random numbers

    Args:
        FILE_SIZE (int): The size of the data set to be generated

    Returns:

    """

    file_name = "size_" + str(FILE_SIZE) + ".txt"

    temp = [i for i in range(1,FILE_SIZE+1)]

    random.shuffle(temp)

    for array_type in ["random","increasing","decreasing"]:
        with open(os.path.join(os.getcwd(), "random", file_name),'w') as f:
            f.write(str(FILE_SIZE))
            f.write('\n')

            if array_type == "random":
                f.writelines([str(i)+'\n' for i in temp])
            elif array_type == "increasing":
                f.writelines([str(i)+'\n' for i in range(1, FILE_SIZE + 1)])
            elif array_type == "decreasing":
                f.writelines([str(i)+'\n' for i in range(FILE_SIZE, 0, -1)])

            f.flush()

def generate_files(FILE_NO : int = 10) -> None:
    """This function will dictate the generation of the files and folders

    Args:
        FILE_NO (int): The number of dataset files that are to be generated
            (default is 10)

    Returns:

    """

    sizes = get_sizes(FILE_NO//2)

    directories = ["random", "increasing", "decreasing", "plots"]
    current_path = os.getcwd()
    for directory in directories:
        path = os.path.join(current_path, directory)
        if directory not in os.listdir():
            os.mkdir(path)

    for size in sizes:
        produce_file(size)