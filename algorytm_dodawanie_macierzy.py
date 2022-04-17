#warunek zadzialania funkcji:macierze musza byc takich samych wymiarow
def Jakub_Wierzbicki_suma_mac(A,B):
    #tworzymy macierz C, ktora bedzie naszym wynikiem
    C = [0] * len(A)
    for i in range(len(C)):
        C[i] = [0]*len(A[i]);
    #dodajemy macierze
    for i in range(len(C)):
        for j in range(len(C[i])):
            C[i][j]=A[i][j]+B[i][j]
    return C
#przykład
A= [[0,0],[1,1],[0,0]]
B=[[1,1],[1,1],[2,2]]
print(Jakub_Wierzbicki_suma_mac(A,B))