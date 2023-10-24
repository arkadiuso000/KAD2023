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
#normalize=True oznacza ze chcemy wynik miec w procentach domyslnie jest false
udzial_procentowy = (myData['species'].value_counts(normalize=True) * 100).round(2)
print("Liczebność poszczególnych gatunków:")
print(liczebnosc_gatunkow)
print("\nUdział procentowy poszczególnych gatunków:")
print(udzial_procentowy)

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

    odchylenieStandardowe = math.sqrt(sumaKwadratowroznic / (len(lista) -1))
    return odchylenieStandardowe
a = [1,2,3,4,5,6]
print(wyznaczOdchylenieStandardowe(a))
