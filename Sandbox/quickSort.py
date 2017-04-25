def quickSort(A,start,end):
    if start<end:
        pivot=hoarePart(A,start,end)
        quickSort(A,start,pivot-1)
        quickSort(A,pivot+1,end)
    return A

def hoarePart(A,start,end):
    pivot=A[start]
    left=start
    right=end
    stop=False
    while not stop:
        while left<=right and A[left]<=pivot:
            left=left+1
        while A[right]>=pivot and left<=right:
            right=right-1
        
        if right<left:
            stop=True
        else:
            aux=A[left]
            A[left]=A[right]
            A[right]=aux

    #Do final Swap
    aux=A[start]
    A[start]=A[right]
    A[right]=aux

    return right

#Testing Purposes
test_array=[8,3,2,9,7,1,5,4]
print quickSort(test_array,0,len(test_array)-1)