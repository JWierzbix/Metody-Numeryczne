def Wierzbicki_Jakub_horner2(a,c):
    #tworzymy tablice wynikowa
    B = [0]*len(a)
    B[0] = a[0]
    for i in range(1,len(a)):
        B[i]= a[i] + c * B[i-1]
    wynik = "W(x)= "
    for i in range(len(a)-1):
        if i==len(a)-2:
            wynik += " ({})".format(B[i], len(a) - 2 - i)
            break
        wynik += " ({})x^{} +".format(B[i],len(a)-2-i)
    return wynik + " ,reszta= {}".format(B[len(a)-1])
a=[2,-1,-7,2]
print(Wierzbicki_Jakub_horner2(a,2))