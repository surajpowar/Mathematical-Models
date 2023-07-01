# Author: Suraj Powar
# Date: 07/1/2023
# Bisection Method for Numerical Approximation.


import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from sympy import *
from math import *

func =  lambda x : x**2 -2

a = 1
b = 3

if func(a)*func(b) > 0:
    print("Could not find the root.")
else: 
    while ((b - a)/2) > 0.00001:
        m = (b + a)/2
        if func(m) == 0:
            print(m)
        elif func(a)*func(m) < 0:
            b = m
        else:
            a = m

print(m)

xvals = np.linspace(-2, 6, num=100)
yvals = func(xvals)
plt.plot(xvals,yvals, label = "y = x^2 - 2")
plt.plot(m, func(m), "o", label = m)
plt.title("Bisection Method for Numerical Approximation")
plt.legend()
plt.show()

