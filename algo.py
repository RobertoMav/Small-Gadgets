#Implementing bubble sort on python 
    # do
    # swapped = false
    # for i = 1 to indexOfLastUnsortedElement-1
    # if leftElement > rightElement
    # swap (leftElement, rightElement)
    # swapped = true; ++swapCounter
    # while swapped

def bubb(array):
    op = 0
    checks = 0
    arr_size = len(array)-1
    swapp = True
    while swapp:

        swapp = False
        for i in range(arr_size):
            checks += 1
            if array[i] > array[i+1]:
                temp = array[i] 
                array[i] = array[i+1]
                array[i+1] = temp
                swapp = True
                op += 1
        arr_size -= 1
            
    return array, op, checks

import numpy as np

a = np.random.randint(50, size=(1,10))
a = a[0].tolist()
print(a)
print(bubb(a))
