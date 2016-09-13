__author__ = 'student'

import numpy as np

import matplotlib.pyplot as plt

xlist = np.arange(-2, 2.01, 0.01)

a = int(input())

b = float(input())


def f(xlist):
    a = np.cos(np.pi * xlist)

    for n in range(50):
        a += (b ** n) * (np.cos((a ** n) * np.pi * xlist))
    return a


plt.plot(xlist, f(xlist))

plt.xlabel(r'$x$')

plt.ylabel(r'$f(x)$')

plt.grid(True)

plt.show()
