def SelectionSort(input_array):
	#We use this line to convert to Array if the input is a string
	#If the input is an Array then nothing changes
    input_array=list(input_array)
    print "The array to sort is " +str(input_array)+"\n"          
    for i in range(0,len(input_array)):
        min=input_array[i]
        for j in range(i+1,len(input_array)):
            if input_array[j]<min:
                print "Current array " +str(input_array)
                print "Current value: "+str(input_array[i])                
                min=input_array[j]
                print "The new minimum is: "+str(min)
                aux=input_array[j]
                input_array[j]=input_array[i]
                input_array[i]=aux
                print "The array now looks like this " +str(input_array)+"\n"

    return input_array

#Testing purposes
array=[3,2,6,4,1,11,9]
SelectionSort(array)