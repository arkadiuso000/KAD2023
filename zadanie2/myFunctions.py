import math
import pandas as pd
import matplotlib.pyplot as plt
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

    plt.scatter(myData[osX], myData[osY], marker="+", c="green" )
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    wspolczynnikKorelacjiPearsona = wyznaczWspolKorelacjiPearsona(myData[osX],myData[osY])
    zaokraglonyWspolczynnik = round(wspolczynnikKorelacjiPearsona,2)
    #TODO zrobic ifa na minusowa wartosc !!!!
    plt.title("r = {}; y = {}x + {}".format(zaokraglonyWspolczynnik,0,0))
    plt.grid(True,linewidth=0.5)
    if xTicks != None:
        plt.xticks(xTicks)
    if yTicks != None:
        plt.yticks(yTicks)

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
    kowariancja = sumaWartosciXYMinusIchSrednie / (n-1)
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