# Sorting Algorithms Benchmarking

## Introduction

This project aims to benchmark the running time of five different sorting algorithms: Heap sort, Insertion sort, Merge sort, Quick sort, and Radix sort. Sorting algorithms are an essential tool in computer science and are used to sort large sets of data efficiently. However, different sorting algorithms have different strengths and weaknesses, and choosing the right algorithm for a particular use case can have a significant impact on performance.

In this project, we will compare the performance of these five sorting algorithms on various data sets to determine which algorithm is the fastest for each scenario. We will measure the time it takes for each algorithm to sort the data set and compare the results using statistical analysis.

## Steps to run the project

The code for all the sorting algorithms as well as the files to execute and plot the graphs are written in `Python 3.10.6`. The given code will only run on a Linux or Unix machine as we have used certain modules that are not available for Windows.

To install the required dependencies first make sure you have python3 and pip3 installed using the command:

```bash
python3 --version
pip3 --version
```
Linux and Unix come pre-installed with python.
If pip3 is not installed then install it using the following commands:

```bash
sudo apt install python3-pip -y
```

Now install the required dependencies using:

```bash
pip3 install -r requirements.txt
```

Now you can run the program using:

```bash
python3 main.py
```

You can now see the data sets in `random`, `increasing` and `decreasing` folders and the graphs of all sorting algorithms in `plots` folder.
