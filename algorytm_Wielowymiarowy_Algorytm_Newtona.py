import numpy
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
from scipy.misc import derivative
#####################################################
########liczenie pochodnej cząstkowej - sposób#######
#####################################################
def f1(x,y):
    return x**2 - 4*y**2 - 4
def f2(x,y):
    return x+y-2
def partial_derivative(func,var=0,point=[]):
    args = point[:]
    def wraps(x):
        args[var] =x
        return func(*args)
    return derivative(wraps,point[var],dx=1e-6)
#####################################################
######################FUNKCJA########################
#####################################################
def Wierzbicki_Jakub_Newton_wielowymiarowy(x,y,eps):
    i=0
    Wk0= np.array([0,0])
    Wk1= np.array([x,y])
    while la.norm(Wk1-Wk0)>eps:
        Wk0=Wk1
        D= np.array( [ [partial_derivative(f1,0,[x,y]),partial_derivative(f1,1,[x,y])] , [partial_derivative(f2,0,[x,y]),partial_derivative(f2,1,[x,y])] ] )
        D_Inverse = np.linalg.inv(D)
        F = np.array([f1(x,y),f2(x,y)])
        Wk1 = Wk0 - D_Inverse.dot(F)
        x=Wk1[0]
        y=Wk1[1]
        i+=1
    return Wk1,i

print(Wierzbicki_Jakub_Newton_wielowymiarowy(1,0,0.01))

x = numpy.linspace(-10,10,10000)
y = numpy.linspace(-10,10,10000)
y1 = x**2 - 4*y**2 - 4
y2 = x+y-2
plt.plot(x,y,y1)
plt.plot(x,y,y2)
plt.show()
