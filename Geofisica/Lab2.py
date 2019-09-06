import numpy as np
import matplotlib.pylab as plt

a = np.genfromtxt("dato1.txt", delimiter = "|")

x = a[:,0]
m = a[:,1]

plt.figure()
plt.plot(x,m)
plt.grid()
plt.xlabel("$x(m)$")
plt.ylabel("$Elevación$ $(m)$")
plt.savefig("elevacion")