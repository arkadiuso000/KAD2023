import numpy as np
import matlib as ml
import statistics as stat
import math
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# wczytuje plik csv
columns = ["sepal lengtha", "sepal width", "petal length", "petal width", "species"]
mapowanie_gatunkow = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}
myData = pd.read_csv("././Dane-20231023/data.csv", header=None, names=columns)
# zamieniam 0,1,2 na odpowiednie nazwy
myData['species'] = myData['species'].replace(mapowanie_gatunkow)

# PUNKT 1.

# oblicza liczebność poszczególnych gatunków
liczebnosc_gatunkow = myData['species'].value_counts()
# oblicza udział procentowy poszczególnych gatunków
# normalize=True oznacza ze chcemy wynik miec w procentach domyslnie jest false
udzial_procentowy = (myData['species'].value_counts(normalize=True) * 100).round(2)
# print("Liczebność poszczególnych gatunków:")
# print(liczebnosc_gatunkow)
# print("\nUdział procentowy poszczególnych gatunków:")
# print(udzial_procentowy)


# PUNKT 2.

def wyznaczMaksimum(lista):
    maksimum = 0
    for wartosc in lista:
        if wartosc > maksimum:
            maksimum = wartosc
    return maksimum


def wyznaczMinimum(lista):
    maksimum = 9999
    for wartosc in lista:
        if wartosc < maksimum:
            maksimum = wartosc
    return maksimum


def wyznaczSredniaArytmetyczna(lista):
    suma = 0
    for wartosc in lista:
        suma += wartosc
    return suma / len(lista)


def wyznaczOdchylenieStandardowe(lista):
    sredniaArytmetyczna = wyznaczSredniaArytmetyczna(lista)

    sumaKwadratowroznic = 0
    for wartosc in lista:
        sumaKwadratowroznic += (wartosc - sredniaArytmetyczna) ** 2

    odchylenieStandardowe = math.sqrt(sumaKwadratowroznic / (len(lista) - 1))
    return odchylenieStandardowe

def wyznaczMediane(lista):
    posortowana_lista = sorted(lista)

    #odejmuje jeden aby dzialac na indeksach tablicy
    srodek = (len(posortowana_lista) - 1) // 2

    if len(posortowana_lista) % 2 == 0:
        return (posortowana_lista[srodek] + posortowana_lista[srodek + 1]) / 2
    else:
        return  float(posortowana_lista[srodek])

def wyznaczTrzyKwartyle(lista):
    # wg prezentacji na wykladzie: W_2_Statystyka_Miary_położenia strona 73
    # wystarczy wywolac metode mediane na polowach posortowanej listy
    # wtedy wyznaczy to pierwszy i trzechi kwartyl
    # sposob ten jest rowniez zgodny z metoda 2 z tego bloga:
    # https://www.statystyczny.pl/jak-obliczamy-kwantyle/

    listaKwartyli = []
    listaPosortowana = sorted(lista)
    srodek = (len(listaPosortowana) - 1) // 2

    listaKwartyli.append(wyznaczMediane(listaPosortowana[:srodek+1]))
    # print("pierwszy podzbior:           {}".format(listaPosortowana[:srodek+1]))
    listaKwartyli.append(wyznaczMediane(listaPosortowana))
    if len(listaPosortowana) % 2 == 0:
        listaKwartyli.append(wyznaczMediane(listaPosortowana[srodek+1:]))
        # print("drugi podzbior:              {}".format(listaPosortowana[srodek+1:]))
    else:
        listaKwartyli.append(wyznaczMediane(listaPosortowana[srodek:]))
        # print("drugi podzbior:              {}".format(listaPosortowana[srodek:]))

    return listaKwartyli

    print()




a = [1, 2, 3, 4, 5, 6, 7]
print("Mediana a: {}".format(wyznaczMediane(a)))
# a = range(0,101)

print("moje kwartyle:       {}".format(wyznaczTrzyKwartyle(a)))

print("numpaja kwartyle:    [{}, {}, {}]".format(np.quantile(a,1/4),np.quantile(a,1/2),np.quantile(a,3/4)))


