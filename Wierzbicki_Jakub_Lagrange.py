import pylab as p
def Wierzbicki_Jakub_Lagrange(x,xw,yw,n):
    w=len(x)*[0]
    W=len(x)*[0]
    for i in range(len(x)):
          for j in range(n): #j to ilosc wezłow , wcześniej: for j in range(len(xw)):
              w[i] = yw[j]
              for k in range(len(xw)):
                  if j==k: continue
                  w[i]*=(x[i]-xw[k])/(xw[j]-xw[k])
              W[i] += w[i]

    return W
Xw=[-2,1,4]
Yw=[5,3,7]
X=[0,3,5]
print(Wierzbicki_Jakub_Lagrange(X,Xw,Yw,3))

#w funkcji używane są Xw i Yw z powyższego przykładu
def Wierzbicki_Jakub_Efekt_Runge(k):
    # dane wejściowe do lagrange
    Xw = [-2, 1, 4,6]
    Yw = [5, 3, 7,9]
    # aregumenty, dla ktorych utworzona funkcja lagrange'a bedzie rysowac wykresy
    X = [0, 3, 5, 7]
    for i in range(k):
        Y = Wierzbicki_Jakub_Lagrange(X,Xw,Yw,i)
        p.plot(X,Y)
    p.show()

print(Wierzbicki_Jakub_Efekt_Runge(3))