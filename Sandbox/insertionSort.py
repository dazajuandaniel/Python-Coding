def insertionSort(A):
    for i in range(1,len(A)):
        v=A[i]
        j=i-1
        print "Checking the array: "+str(A)
        print "Comparing against "+str(v)
        while j>=0 and A[j]>v:
            print "Moving "+str(A[j]) +" to the right"
            A[j+1]=A[j]
            j=j-1
        A[j+1]=v
        print "The Array is now: "+str(A)+"\n"
    return A

#Testing purposes
test_array=[7,5,3,9,10,15,1,4,2]
print insertionSort(test_array)