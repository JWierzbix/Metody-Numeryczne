#uwaga: funkcja zadziala tylko wtedy,gdy macierze sa w relacji:
# 1. liczba kolumn macierzy A rowna sie liczbie wierszy macierzy B
# 2. liczba wierszy macierzy A rowna sie liczbie kolumn macierzy B
def Jakub_Wierzbicki_mnoz_mac(A,B):
    #deklarujemy macierz wynikowa:
    C = [0]*len(A)
    for i in range(len(C)):
        C[i] = [0]*len(B[i])
    #wykonujemy mnozenie macierzy
    for i in range(len(A)):
        for j in range(len(B[i])):
            for k in range(len(B[i])):
                C[i][j]+=A[i][k]*B[k][j]
    return C
A= [[2,1,3],[-1,4,0]]
B= [[1,3,2],[-2,0,1],[5,-3,2]]
print(Jakub_Wierzbicki_mnoz_mac(A,B))