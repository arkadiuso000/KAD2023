import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def importData(fileDst):
    columns = ["sepal length", "sepal width", "petal length", "petal width", "species"]
    mapowanie_gatunkow = {
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }
    myData = pd.read_csv(fileDst, header=None, names=columns)
    # zamieniam 0,1,2 na odpowiednie nazwy
    myData['species'] = myData['species'].replace(mapowanie_gatunkow)
    return myData

def generatePlot(myData, osX, osY,xLabel,yLabel,xTicks,yTicks):
    plt.figure(figsize=(10, 7))
    plt.scatter(myData[osX], myData[osY], c="green" )
    plt.xlabel(xLabel, fontsize=20,)
    plt.ylabel(yLabel, fontsize=20,)
    wspolczynnikKorelacjiPearsona = wyznaczWspolKorelacjiPearsona(myData[osX],myData[osY])
    zaokraglonyWspolczynnik = round(wspolczynnikKorelacjiPearsona,2)
    rowanieRegresji = wyznaczRownanieRegresjiLiniowej(myData[osX],myData[osY])
    aRound1 = round(rowanieRegresji[0],1)
    bRound1 = round(rowanieRegresji[1],1)

    if (bRound1 < 0):
        plt.title("r = {}; y = {}x - {}".format(zaokraglonyWspolczynnik,aRound1,abs(bRound1)), fontsize=20,)
    else:
        plt.title("r = {}; y = {}x + {}".format(zaokraglonyWspolczynnik,aRound1,bRound1), fontsize=20,)
    plt.grid(True,linewidth=0.5, alpha=0.45,)

    #dodawanie wykresu regresji liniowej
    plt.plot(myData[osX], rowanieRegresji[0] * myData[osX] + rowanieRegresji[1], color='red', alpha=0.75, )
    if xTicks != None:
        plt.xticks(xTicks)
    if yTicks != None:
        plt.yticks(yTicks)
    ax = plt.subplot()
    ax.set_xticklabels(xTicks, fontsize=16)
    ax.set_yticklabels(yTicks, fontsize=16)
    # ax.set_xticklabels(x, fontsize=16)

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

def wyznaczRownanieRegresjiLiniowej(listaX, listaY):
    a = wyznaczKowariancje(listaX,listaY) / wyznaczWariancje(listaX)
    b = wyznaczSredniaArytmetyczna(listaY) - a * wyznaczSredniaArytmetyczna(listaX)
    return (a,b)
def wyznaczWspolKorelacjiPearsona(listaX, listaY):
    kowariancja = wyznaczKowariancje(listaX, listaY)
    odchylenieStandardoweX = wyznaczOdchylenieStandardowe(listaX)
    odchylenieStandardoweY = wyznaczOdchylenieStandardowe(listaY)
    wspolczynnik = kowariancja / (odchylenieStandardoweX * odchylenieStandardoweY)
    return wspolczynnik
def wyznaczKowariancje(listaX,listaY):
    n = len(listaX)
    if n != len(listaY):
        raise ValueError("Listy musza miec po tyle samo wartosci do obliczenia Kowariancji")
    sredniaArytX = wyznaczSredniaArytmetyczna(listaX)
    sredniaArytY = wyznaczSredniaArytmetyczna(listaY)
    sumaWartosciXYMinusIchSrednie = 0
    for i in range(n):
        sumaWartosciXYMinusIchSrednie += ((listaX[i] - sredniaArytX) * (listaY[i] - sredniaArytY))
    kowariancja = sumaWartosciXYMinusIchSrednie / (n)
    #tutaj ogolnie powinno byc -1 aby kowariancja byla sama w sobie git
    #lecz do pearsona potrzebujemy n-1 gdyz tak wynika z przeksztalcen
    #aby to uzyc w przyszlosci musze to poprawic!
    return kowariancja

def wyznaczWariancje(lista):
    sredniaArytmetyczna = wyznaczSredniaArytmetyczna(lista)

    sumaKwadratowroznic = 0
    for wartosc in lista:
        sumaKwadratowroznic += (wartosc - sredniaArytmetyczna) ** 2

    wariancja = sumaKwadratowroznic / (len(lista))
    return wariancja
def wyznaczOdchylenieStandardowe(lista):
    odchylenieStandardowe = math.sqrt(wyznaczWariancje(lista))
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
    listaKwartyli.append(wyznaczMediane(listaPosortowana))
    if len(listaPosortowana) % 2 == 0:
        listaKwartyli.append(wyznaczMediane(listaPosortowana[srodek + 1:]))
    else:
        listaKwartyli.append(wyznaczMediane(listaPosortowana[srodek:]))
    return listaKwartyli