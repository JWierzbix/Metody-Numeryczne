import math
def Wierzbicki_Jakub_gauss_pivot(A,b):
    for k in range(len(A[0])):
        #szukam elementu o najwiekszej wartosci
        max_value= -1*math.inf
        max_indx =0;
        for i in range(len(A)):
           if max_value < A[i][k]:
               max_value= A[i][k]
               max_indx= i
        #dziele caly wiersz, ktorego element mial maksymalna wartosc
        for j in range(k,len(A[0])):
            A[max_indx][j] /= max_value
        b[max_indx] /= max_value
        #wykonuje eliminacje gaussa po wierszach
        for i in range(len(A)):
            if i == max_indx: continue
            dzielnik=A[i][k]
            for j in range(k,len(A[i])):
                A[i][j] -= dzielnik*A[max_indx][j]
            b[i] -= dzielnik*b[max_indx]
    return b
#przyklad
A=[[2,-3,-1],[-4,10,5],[8,-4,4]]
b=[9,-29,12]
print(Wierzbicki_Jakub_gauss_pivot(A,b))