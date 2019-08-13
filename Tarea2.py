import numpy as np
import time
import matplotlib.pylab as plt

def fib_recursion(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)
    
list_n = []
list_time = []
for i in range(1,40):
    init= time.time()
    print (fib_recursion(i))
    difference = time.time()-init
    list_n.append(i)
    list_time.append(difference)

    
plt.figure()
plt.plot(list_n, list_time)
