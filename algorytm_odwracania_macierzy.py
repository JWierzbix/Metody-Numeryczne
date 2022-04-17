def Wierzbicki_Jakub_macierz_odwrotna(A):
    #tworzymy wspolna macierz
    M=(len(A))*[0]
    for i in range(len(A)):
        M[i]=(2*len(A[i]))*[0]
    #uzupelniamy macierz M
    for i in range(len(A)):
        M[i][len(A[i])+i]=1
        for j in range(len(A[i])):
            M[i][j] = A[i][j]
    # wykonujemy eliminacje gaussa
    for k in range(len(M)):
        dzielnik = M[k][k]
        for i in range(k, len(M[k])):
            M[k][i] /= dzielnik
        for i in range(len(M)):
            if k == i: continue
            mnoznik = M[i][k]
            for j in range(k, len(M[i])):
                M[i][j] -= mnoznik * M[k][j]
    #wyznaczamy macierz odwrotna
    MD=len(A)*[0]
    for i in range(len(A)):
        MD[i]=len(A[i])*[0]
    for i in range(len(A)):
        for j in range(len(A[i])):
            MD[i][j]=round(M[i][len(A[i])+j])
    return MD
#przyklad
A=[[2,5,7],[6,3,4],[5,-2,-3]]
print(Wierzbicki_Jakub_macierz_odwrotna(A))
