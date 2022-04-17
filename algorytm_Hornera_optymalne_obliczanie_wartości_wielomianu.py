#wspolczyniki zapisujemy w kolejnosci - zaczynajac od tego, ktorego potega jest najwieksza.
#na przyklad: x^2+2x+3 => {1,2,3}
def Wierzbicki_Jakub_horner(a,x):
    if len(a)==0 : return 0 #przypadek, gdy tablica bedzie pusta
    wynik = 0;
    for i in range(len(a)-1):
        wynik = (wynik+a[i])*x
    wynik+= a[len(a)-1]
    return wynik
#przyklad
a=[3,2,-7]  #W(x)= 3x^2 + 2x - 7
print(Wierzbicki_Jakub_horner(a,2))