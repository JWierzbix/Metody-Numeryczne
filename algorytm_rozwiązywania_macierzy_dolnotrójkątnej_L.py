def Wierzbicki_Jakub_ukladL(L,b):
    #deklarujemy macierz wynikową X
    X = [0]*len(L[0])
    #rozwiazujemy uklad rownan
    for i in range(len(L)):
        X[i] = b[i]
        for j in range(i):
            if j==i: continue
            X[i] -= L[i][j]*X[j]
        X[i] /= L[i][i]
    return X
#przyklad
L=[[1,0,0],[2,2,0],[3,3,2]]
b=[2,8,6]
print(Wierzbicki_Jakub_ukladL(L,b))