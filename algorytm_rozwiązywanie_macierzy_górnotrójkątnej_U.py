def Wierzbicki_Jakub_ukladU(U,b):
    #deklarujemy tablice wynikow naszego ukladu rownan
    X = [0]*len(U[0])
    for i in range(len(U)):
        k = len(U)-i-1 #deklarujemy zmienna pomocnicza
        X[k] = b[k]
        for j in range(i):
            l = len(U[k])-1-j #deklarujemy druga zmienna pomocnicza
            if l==k: continue
            X[k] -= U[k][l]*X[l]
        X[k] /= U[k][k]
    return X
#przyklad
U=[[2,3,3],[0,2,2],[0,0,1]]
b=[6,8,2]
print(Wierzbicki_Jakub_ukladU(U,b))