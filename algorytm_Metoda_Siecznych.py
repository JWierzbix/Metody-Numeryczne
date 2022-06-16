import math
import pylab as p
def f(x):
    return x*x*x-2*x*x-2
def Wierzbicki_Jakub_sieczne(x1,x2,eps):
    Bx=[-4,-3,-2,-1,0,1,2,3,4]
    By=[f(-4),f(-3),f(-2),f(-1),f(0),f(1),f(2),f(3),f(4)]
    p.plot(Bx,By)
    i=0
    j=0
    A= (10000)*[0]
    while math.fabs(x2-x1) > eps:
        x3 = x2 - ((x2-x1)/(f(x2)-f(x1)))*f(x2)
        x1=x2
        x2=x3
        A[j]=x1
        A[j+1]=x2
        j+=2
        i+=1
    for k in range(j):
        X=[A[k],A[k+1]]
        Y=[f(A[k]),f(A[k+1])]
        p.plot(X, Y)
        k+=2
    p.show()
    return "x0 = {} and {} iterations".format(x2,i)

print(Wierzbicki_Jakub_sieczne(2,1,0.01))