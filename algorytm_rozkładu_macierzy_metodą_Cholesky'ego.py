import math
#macierz musi byc symetryczna i dodatnio okreslona
def Wierzbicki_Jakub_rozklad_cholseky(A):
    #wyznaczamy macierze trojkatne
    L=len(A)*[0]
    for i in range(len(A)):
        L[i]=len(A[i])*[0]
    U=len(A)*[0]
    for i in range(len(A)):
        U[i]=len(A[i])*[0]
    #dokonujemy rozkladu LU
    for j in range(len(A[0])):
        for i in range(j,len(A)):
            if i==j:
                L[i][j] = A[i][j]
                for k in range(i):
                    L[i][j] -= L[i][k]*L[i][k]
                L[i][j] = math.sqrt(L[i][j])
                U[i][j] = L[i][j]
            if i!=j:
                L[i][j] = A[i][j]
                for k in range(j):
                    L[i][j] -= L[i][k]*L[j][k]
                L[i][j] /= L[j][j]
                U[j][i] = L[i][j]
    return L,U
#przyklad
A=[[1,2,3],[2,13,9],[3,9,14]]
print(Wierzbicki_Jakub_rozklad_cholseky(A))