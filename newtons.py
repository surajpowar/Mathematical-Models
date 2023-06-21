# Author: Suraj Powar
# Date: 06/21/2023
# Newton's Method for Numerical Approximation.


import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from sympy import *
from math import *

func =  lambda x : x**2 -2
funcprime = lambda x: 2*x 

#initial Guess
x0 = 2
iteration = 20
x1 = x0

guess = []
for i in range(1,iteration):
    x1 = x1 - (func(x1)/funcprime(x1))
    guess = [guess, x1]

print(x1)
print(np.sqrt(2) - x1)

xvals = np.linspace(-2, 3, num=100)
yvals = func(xvals)
plt.plot(xvals,yvals)
plt.plot(x1, func(x1), "o")
plt.title("Newtons Method for Numerical Approximation")
plt.show()

