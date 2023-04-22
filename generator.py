import random
import os

def get_sizes(MAX_POWER_OF_10 : int = 6,FOLD_INCREASE : int = 3) -> list:
    """
        This function generators the different sizes of the input files.
        We will be taking the input sizes increasing by three-fold(default)
    """
    sizes = []

    for i in range(1,MAX_POWER_OF_10+1):
        sizes.append(int(10**i/FOLD_INCREASE))
        sizes.append(10**i)

    return sizes

def produce_file(FILE_SIZE : int):
    file_name = "size_" + str(FILE_SIZE) + ".txt"

    temp = [i for i in range(1,FILE_SIZE+1)]

    random.shuffle(temp)
    
    with open(os.path.join(os.getcwd(), "random", file_name),'w') as f:
        f.write(str(FILE_SIZE))
        f.write('\n') 

        f.writelines([str(i)+'\n' for i in temp])
        f.flush()
    
    with open(os.path.join(os.getcwd(), "increasing", file_name),'w') as f:
        f.write(str(FILE_SIZE))
        f.write('\n')

        f.writelines([str(i)+'\n' for i in range(1, FILE_SIZE + 1)])
        f.flush()
    
    with open(os.path.join(os.getcwd(), "decreasing", file_name),'w') as f:
        f.write(str(FILE_SIZE))
        f.write('\n')

        f.writelines([str(i)+'\n' for i in range(FILE_SIZE, 0, -1)])
        f.flush()

def generate_files(FILE_NO : int):
    sizes = get_sizes(FILE_NO//2)

    directories = ["random", "increasing", "decreasing"]
    current_path = os.getcwd()
    for directory in directories:
        path = os.path.join(current_path, directory)
        os.mkdir(path)

    for size in sizes:
        produce_file(size)
    
generate_files(12)