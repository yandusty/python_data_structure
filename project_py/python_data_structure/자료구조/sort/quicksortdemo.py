from QuickSort import *
from MergeSort import *

def do_sort(input_file):
    data_file = open(input_file)
    A = []
    value = []
    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn not in A:
            A[lpn] = 1
        else:
            A[lpn] += 1
    
    for key in A:
        value.append(A[key])
    value.sort()

    for i in range(10):
        print(value.pop())
    print("")
'''
    for i in range(10):
        print(A[i], end=" ")
    print("")

    quickSort(A,0,len(A)-1)

    for i in range(10):
        print(A[i], end=" ")
    print("")
'''
if __name__ == "__main__":
    do_sort("linkbench_short.trc")