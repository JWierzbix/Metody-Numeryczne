import math
def f(x):
    return 12*x*x*x - 95*x*x + 77*x
#funkcja na przedziale [a,b] musi mieć jedno rozwiązanie
def Wierzbicki_Jakub_bisekcja(a,b,eps):
    while math.fabs(b-a)>eps:
        if a>b:
            c=a
            a=b
            b=a
        s = a + math.fabs(b-a)/2
        if f(s) == 0:
            return s
        elif f(a)*f(s) < 0:
            b = s
        else:
            a = s
    return a + math.fabs(b-a)/2
print(Wierzbicki_Jakub_bisekcja(6,8,0.001))