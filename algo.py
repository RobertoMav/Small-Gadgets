#Random arrow selector
import random
import numpy as np

def random_arrow():

    a = random.random()
    if a <= 0.25:
        b = 0
    elif a <= 0.5:
        b = 1
    elif a <= 0.75:
        b = 2
    else:
        b = 3
    return a, b

ans = []
for i in range(100):
    _, b = random_arrow()
    ans.append(b)

val, count = np.unique(ans, return_counts=True)
count_a = count/np.sum(count)
print(val, count_a, count, np.sum(count))


## Bubble sort implementation
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
                checks += 1
        arr_size -= 1
            
    return array, op, checks

import numpy as np

a = np.random.randint(50, size=(1,10))
a = a[0].tolist()
print(a)
print(bubb([100, 90,80, 70 ,60 ,50,40,30,20,10]))
#Worst case n * (n-1) = n**2 - n
#Best case n-1 = n