def quickSort(A,B,p:int, r:int):
    if p<r:
        q = partition(A,B,p,r)
        quickSort(A,B,p,q-1)
        quickSort(A,B,q+1,r)

def partition(A,B,p:int,r:int) -> int:
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <x:
            i+= 1
            A[i],A[j] = A[j],A[i]
            B[i],B[j] = B[j],B[i]
    A[i+1],A[r] = A[r], A[i+1]
    B[i+1],B[r] = B[r], B[i+1]
    return i+1
