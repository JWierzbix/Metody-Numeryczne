def Wierzbicki_Jakub_gauss_jordan(A,b):
    #tworzymy wspolna macierz
    M=(len(A))*[0]
    for i in range(len(A)):
        M[i]=(len(A)+1)*[0]
    #uzupelniamy macierz M
    for i in range(len(A)):
        for j in range(len(A[i])):
            M[i][j] = A[i][j]
        M[i][len(M[0])-1]=b[i]
    #wykonujemy eliminacje gaussa
    for k in range(len(M)):
        dzielnik = M[k][k]
        for i in range(k,len(M[k])):
            M[k][i] /= dzielnik
        for i in range(len(M)):
            if k==i: continue
            mnoznik = M[i][k]
            for j in range(k,len(M[i])):
                M[i][j] -= mnoznik*M[k][j]
    #tworzymy macierz wynikowa
    X=len(A[0])*[0]
    for i in range(len(A[0])):
        X[i]=M[i][len(M[0])-1]
    return X
#przyklad
A=[[-1,2,1],[1,-3,-2],[3,-1,-1]]
b=[-1,-1,4]
print(Wierzbicki_Jakub_gauss_jordan(A,b))