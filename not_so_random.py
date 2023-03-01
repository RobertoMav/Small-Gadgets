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