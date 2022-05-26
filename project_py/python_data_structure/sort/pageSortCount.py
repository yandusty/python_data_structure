from quickSort_3 import *

def  do_sort(input_file):

    data_file = open(input_file)
    A={}
    B =[]
    C=[]
    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn in A:
            A[lpn] += 1
        else:
            A[lpn] =1
    for key in A.keys():
        C.append(key)
    for item in A.values():
        B.append(item)

    quickSort(B,C)
           
    for i in range(len(B)-1,len(B)-11,-1):
        print(C[i],B[i],sep = " ", end="\n")



if __name__== "__main__":
    do_sort("linkbench_short.trc")
