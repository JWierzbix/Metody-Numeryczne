import math
def Wierzbicki_Jakub_heron(a,x,eps):
    X=x+1 #deklarujemy zmienna pomocnicza X
    while(math.fabs(X-x)>eps):
        x=X
        X=0.5*(x+a/x)
    return X
print(Wierzbicki_Jakub_heron(4,4,0.001))