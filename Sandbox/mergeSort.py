def mergeSort(A):
    n=len(A)
    mid=n/2
    if n>1:
        #Copy A[0...n/2-1] to B[0...n/2-1]
        leftside=A[:mid]
        #Copy A[n/2...n] to C[0...n/2]
        rightside=A[mid:]
        #Do recursion to split the array
        print "MergeSorting: "+str(leftside)
        mergeSort(leftside)
        print "MergeSorting: "+str(rightside)
        mergeSort(rightside)
        print "Going to Merge: " +str(A)
        merge(leftside,rightside,A)
    return A

def merge(B,C,A):
    i=0
    j=0
    k=0
    lenB=len(B)
    lenC=len(C)
    n=len(A)
    while i<lenB and j<lenC:
        if B[i]<=C[j]:
            A[k]=B[i]
            i=i+1
        else:
            A[k]=C[j]
            j=j+1
        k=k+1
    #Copy C[j...lenC-1] to A[k...lenB+lenC+1]
    while j<lenC:
            A[k]=C[j]
            j=j+1
            k=k+1
    #Copy B[i...lenB-1] to A[k...lenB+lenC+1]
    while i<lenB:
            A[k]=B[i]
            i=i+1
            k=k+1
    print "Merged: "+str(A)
    return A

test_array=[8,3,2,9,7,1,5,4]
print mergeSort(test_array) 