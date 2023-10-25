import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
import math
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# wczytuje plik csv
columns = ["sepal length", "sepal width", "petal length", "petal width", "species"]
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
caloscLiczba = myData['species'].value_counts().sum()

# oblicza udział procentowy poszczególnych gatunków
# normalize=True oznacza ze chcemy wynik miec w procentach domyslnie jest false
udzial_procentowy = (myData['species'].value_counts(normalize=True) * 100).round(2)
calosProcent = (myData['species'].value_counts(normalize=True) * 100).sum()
print("\tPUNKT 1\n")
print("Liczebność poszczególnych gatunków:")
print(liczebnosc_gatunkow)
print("Razem: {}".format(caloscLiczba))
print("\nUdział procentowy poszczególnych gatunków [%]:")
print(udzial_procentowy)
print("Razem: {}".format(math.ceil(calosProcent)))

print("\n\n")


# PUNKT 2.

def wyznaczMaksimum(lista):
    maksimum = lista[0]
    for wartosc in lista:
        if wartosc > maksimum:
            maksimum = wartosc
    return maksimum


def wyznaczMinimum(lista):
    maksimum = lista[0]
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

    # odejmuje jeden aby dzialac na indeksach tablicy
    srodek = (len(posortowana_lista) - 1) // 2

    if len(posortowana_lista) % 2 == 0:
        return (posortowana_lista[srodek] + posortowana_lista[srodek + 1]) / 2
    else:
        return float(posortowana_lista[srodek])


def wyznaczTrzyKwartyle(lista):
    # wg prezentacji na wykladzie: W_2_Statystyka_Miary_położenia strona 73
    # wystarczy wywolac metode mediane na polowach posortowanej listy
    # wtedy wyznaczy to pierwszy i trzechi kwartyl
    # sposob ten jest rowniez zgodny z metoda 2 z tego bloga:
    # https://www.statystyczny.pl/jak-obliczamy-kwantyle/

    listaKwartyli = []
    listaPosortowana = sorted(lista)
    srodek = (len(listaPosortowana) - 1) // 2

    listaKwartyli.append(wyznaczMediane(listaPosortowana[:srodek + 1]))
    # print("pierwszy podzbior:           {}".format(listaPosortowana[:srodek+1]))
    listaKwartyli.append(wyznaczMediane(listaPosortowana))
    if len(listaPosortowana) % 2 == 0:
        listaKwartyli.append(wyznaczMediane(listaPosortowana[srodek + 1:]))
        # print("drugi podzbior:              {}".format(listaPosortowana[srodek+1:]))
    else:
        listaKwartyli.append(wyznaczMediane(listaPosortowana[srodek:]))
        # print("drugi podzbior:              {}".format(listaPosortowana[srodek:]))

    return listaKwartyli

dlugoscDzialki = "\tDługość działki kielicha (cm)\nMinimum:            {}\nSr arytm + odch:    {} +- {}\nMediana(Q1,Q2,Q3):  {}\nMaksimum:           {}\n\n".format(
    wyznaczMinimum(myData["sepal length"]), wyznaczSredniaArytmetyczna(myData["sepal length"]),
    wyznaczOdchylenieStandardowe(myData["sepal length"]), wyznaczTrzyKwartyle(myData["sepal length"]),
    wyznaczMaksimum(myData["sepal length"]))
szerokoscDzialki = "\tSzerokość działki kielicha (cm)\nMinimum:            {}\nSr arytm + odch:    {} +- {}\nMediana(Q1,Q2,Q3):  {}\nMaksimum:           {}\n\n".format(
    wyznaczMinimum(myData["sepal width"]), wyznaczSredniaArytmetyczna(myData["sepal width"]),
    wyznaczOdchylenieStandardowe(myData["sepal width"]), wyznaczTrzyKwartyle(myData["sepal width"]),
    wyznaczMaksimum(myData["sepal width"]))
dlugoscPlatka = "\tDługość płatka (cm)\nMinimum:            {}\nSr arytm + odch:    {} +- {}\nMediana(Q1,Q2,Q3):  {}\nMaksimum:           {}\n\n".format(
    wyznaczMinimum(myData["petal length"]), wyznaczSredniaArytmetyczna(myData["petal length"]),
    wyznaczOdchylenieStandardowe(myData["petal length"]), wyznaczTrzyKwartyle(myData["petal length"]),
    wyznaczMaksimum(myData["petal length"]))
szerokoscPlatka = "\tSzerokość płatka (cm)\nMinimum:            {}\nSr arytm + odch:    {} +- {}\nMediana(Q1,Q2,Q3):  {}\nMaksimum:           {}\n\n".format(
    wyznaczMinimum(myData["petal width"]), wyznaczSredniaArytmetyczna(myData["petal width"]),
    wyznaczOdchylenieStandardowe(myData["petal width"]), wyznaczTrzyKwartyle(myData["petal width"]),
    wyznaczMaksimum(myData["petal width"]))
print("\tPUNKT 2\n")
print(dlugoscDzialki)
print(szerokoscDzialki)
print(dlugoscPlatka)
print(szerokoscPlatka)

# PUNKT 3. - wykresy


nazwyWykresow = ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]
        #dlugosc dzialki kielicha
#rozmiar calego obrazka
plt.figure(figsize=(16, 8))
#tworzy dwa wykresy na jednym obrazku
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

                        #rysowanie histogramu
axs[0].hist(myData[columns[0]], bins=10, alpha=0.5, edgecolor='black', color='green')
#ustawia os x
axs[0].set_xlim(4.0,8.0)
#wlacza siatke
axs[0].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[0].set_ylabel('Liczebność',fontsize=16, fontweight='bold')
axs[0].set_xlabel('Długość (cm)',fontsize=16, fontweight='bold')
axs[0].set_title(nazwyWykresow[0],fontsize=16, fontweight='bold')

                        #rysowanie wykresu pudelkowego

#tworzy dane do wykresu
data1 = list(myData['species'].drop_duplicates())
data2 = [myData[myData['species'] == data1[0]]['sepal length'],
         myData[myData['species'] == data1[1]]['sepal length'],
         myData[myData['species'] == data1[2]]['sepal length']]
#oznaczenia na osi x

#wlacza siatke
axs[1].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[1].boxplot(data2, labels=data1,)
axs[1].set_ylabel('Długość (cm)', fontsize=16, fontweight='bold')
axs[1].set_xlabel("Gatunek", fontsize=16, fontweight='bold')


#zapewnia odpowiednie odstępy między wykresami
plt.tight_layout()
plt.show()


