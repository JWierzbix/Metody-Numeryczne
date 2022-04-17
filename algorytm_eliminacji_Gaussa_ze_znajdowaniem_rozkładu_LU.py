def Wierzbicki_Jakub_gauss(A, b):
    # tworzymy macierz dolnotrojkatna
    L = len(A) * [0]
    for i in range(len(A)):
        L[i] = len(A[i]) * [0]
    # tworzymy macierz gornotrojkatna
    U = len(A) * [0]
    for i in range(len(A)):
        U[i] = len(A[i]) * [0]
    # uzupelniamy jedynkami na diagonali
    for i in range(len(L)):
        L[i][i] = 1
        # uzupelniamy L i U
    # j-kolumny, i-wiersze
    for j in range(len(A[0])):
        for i in range(len(A)):
            if i <= j:
                U[i][j] = A[i][j]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]
            if i > j:
                L[i][j] = A[i][j]
                for k in range(j):
                    L[i][j] -= L[i][k] * U[k][j]
                L[i][j] /= U[j][j]
    # rozwiazujemy 1 uklad rownan: Ly=b
    Y = len(L) * [0]
    for i in range(len(L)):
        Y[i] = b[i]
        for j in range(len(L[i])):
            if i == j: continue
            Y[i] -= L[i][j] * Y[j]
        Y[i] /= L[i][i]
    # rozwiazujemy drugi uklad rownan Ux=y
    X = [0] * len(U[0])
    for i in range(len(U)):
        m = len(U) - i - 1
        X[m] = Y[m]
        for j in range(i + 1):
            n = len(U[m]) - 1 - j
            if m == n: continue
            X[m] -= U[m][n] * X[n]
        X[m] /= U[m][m]
    return X


# przyklad:
A = [[-1, 2, 1], [1, -3, -2], [3, -1, -1]]
b = [-1, -1, 4]
print(Wierzbicki_Jakub_gauss(A, b))