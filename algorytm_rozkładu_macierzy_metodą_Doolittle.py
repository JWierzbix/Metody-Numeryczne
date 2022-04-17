def Wierzbicki_Jakub_doolittle(A):
    #tworzymy macierz dolnotrojkatna
    L=len(A)*[0]
    for i in range(len(A)):
        L[i] = len(A[i])*[0]
    #tworzymy macierz gornotrojkatna
    U=len(A)*[0]
    for i in range(len(A)):
        U[i] = len(A[i])*[0]
    #uzupelniamy jedynkami na diagonali
    for i in range(len(L)):
        L[i][i]=1
    #uzupelniamy L i U
    #j-kolumny, i-wiersze
    for j in range(len(A[0])):
        for i in range(len(A)):
            if i<=j:
                U[i][j]=A[i][j]
                for k in range(i):
                    U[i][j]-=L[i][k]*U[k][j]
            if i>j:
                L[i][j]=A[i][j]
                for k in range(j):
                    L[i][j]-=L[i][k]*U[k][j]
                L[i][j] /= U[j][j]
    return L
#przyklad:
A=[[1,4,7],[2,5,8],[3,6,9]]
print(Wierzbicki_Jakub_doolittle(A))