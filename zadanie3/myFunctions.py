import math
import random
from matplotlib import ticker
import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import copy

#zad 3 podpunkt 2
def podpunkt2PoszczegolneCechy(dataTrainX, dataTrainY,dataTestX, dataTestY):
    #wybieramy wszystkie cechy
    trainX = dataTrainX.values
    trainY = dataTrainY.values
    testX = dataTestX.values
    testY = dataTestY.values

    #tutaj normalizujemy dane
    scaler = StandardScaler()
    trainX = scaler.fit_transform(trainX)
    testX = scaler.transform(testX)


    listaDokladnosci = []

    for k in range(1, 16):
        #tworze i trenuje
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(trainX, trainY)

        # Przewidywanie etykiet dla danych testowych
        dopasowania = knn.predict(testX)

        # Obliczanie i przechowywanie dokładności
        dokladnosc = accuracy_score(testY, dopasowania)
        listaDokladnosci.append(dokladnosc)

    najlepszeK = listaDokladnosci.index(max(listaDokladnosci)) + 1  #1 dodaje bo lista indexuje od 0

    # Utworzenie macierzy pomyłek dla najlepszego k
    najlepszeKNN = KNeighborsClassifier(n_neighbors=najlepszeK)
    najlepszeKNN.fit(trainX, trainY)
    najlepszeDopasowania = najlepszeKNN.predict(testX)
    macierzPomylekDlaNajlepszegoK = confusion_matrix(testY, najlepszeDopasowania)

    # Rysowanie wykresu dokładności
    # Rysowanie wykresu słupkowego dokładności
    plt.figure(figsize=(12, 8))
    plt.bar(range(1, 16), [acc * 100 for acc in listaDokladnosci], color='skyblue', edgecolor='black')
    plt.xlabel('Liczba sąsiadów k',fontsize=18)
    plt.ylabel('Dokładność [%]',fontsize=18)
    plt.xticks(range(1, 16))
    plt.yticks(range(0, 110, 10))
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    zapiszWykres('wykres')
    plt.show()


    print("Najlepsza wartość k:", najlepszeK)
    print("Macierz pomyłek dla najlepszego k:")
    print(macierzPomylekDlaNajlepszegoK)
def podpunkt2WszystkieCechy(dataTrain,dataTest):
    #wybieramy wszystkie cechy
    trainX = dataTrain.iloc[:, :-1].values
    trainY = dataTrain.iloc[:, -1].values
    testX = dataTest.iloc[:, :-1].values
    testY = dataTest.iloc[:, -1].values

    #tutaj normalizujemy dane
    scaler = StandardScaler()
    trainX = scaler.fit_transform(trainX)
    testX = scaler.transform(testX)


    listaDokladnosci = []

    for k in range(1, 16):
        #tworze i trenuje
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(trainX, trainY)

        # Przewidywanie etykiet dla danych testowych
        dopasowania = knn.predict(testX)

        # Obliczanie i przechowywanie dokładności
        dokladnosc = accuracy_score(testY, dopasowania)
        listaDokladnosci.append(dokladnosc)

    najlepszeK = listaDokladnosci.index(max(listaDokladnosci)) + 1  #1 dodaje bo lista indexuje od 0

    # Utworzenie macierzy pomyłek dla najlepszego k
    najlepszeKNN = KNeighborsClassifier(n_neighbors=najlepszeK)
    najlepszeKNN.fit(trainX, trainY)
    najlepszeDopasowania = najlepszeKNN.predict(testX)
    macierzPomylekDlaNajlepszegoK = confusion_matrix(testY, najlepszeDopasowania)

    # Rysowanie wykresu dokładności
    # Rysowanie wykresu słupkowego dokładności
    plt.figure(figsize=(12, 8))
    plt.bar(range(1, 16), [acc * 100 for acc in listaDokladnosci], color='skyblue', edgecolor='black')

    plt.xlabel('Liczba sąsiadów k',fontsize=18)
    plt.ylabel('Dokładność [%]',fontsize=18)
    plt.xticks(range(1, 16))
    plt.yticks(range(0, 110, 10))
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    zapiszWykres('wykres')
    plt.show()

    print("Najlepsza wartość k:", najlepszeK)
    print("Macierz pomyłek dla najlepszego k:")
    print(macierzPomylekDlaNajlepszegoK)










#zad 3 podpunkt 1
iteracje = []
def kSrednich(dane, k, czyPokazacWykres=False):
    centroidy = inicjacjaCentroidow(dane,k)
    kopiaDanych = copy.deepcopy(dane)
    iloscIteracji = 0
    while True:
        iloscIteracji += 1
        poprzednieCentroidy = centroidy
        klastry = przypiszKlastry(kopiaDanych, centroidy)
        centroidy = aktualizacjaCentroidow(kopiaDanych, klastry, k)

        if warunekStopu(poprzednieCentroidy,centroidy):
            break
    iteracje.append(iloscIteracji)
    for i in range(len(kopiaDanych)):
        kopiaDanych[i].append(klastry[i])
        kopiaDanych[i].append(centroidy[klastry[i]])

    #funkcja zwraca nam poczatkowe dane z dodana kolumna klastrow
    columns = ["sepal length", "sepal width", "petal length", "petal width", "cluster", "centroid"]
    # print(dane)
    df = pd.DataFrame(kopiaDanych, columns=columns)

    dfToList = df.values.tolist()


    if k==0:
        #generowanie wykresow
        #1st
        generujWykresKSrednich(centroidy,df,"sepal length", "sepal width", "Długość działki kielicha (cm)","Szerokość dzialki kielicha (cm)")
        #2nd
        generujWykresKSrednich(centroidy,df,"sepal length", "petal length", "Długość działki kielicha (cm)", "Długość płatka (cm)")
        #3rd
        generujWykresKSrednich(centroidy,df,"sepal length", "petal width", "Długość działki kielicha (cm)", "Szerokość płatka (cm)")
        #4th
        generujWykresKSrednich(centroidy,df,"sepal width", "petal length", "Szerokość działki kielicha (cm)", "Długość płatka (cm)")
        #5th
        generujWykresKSrednich(centroidy,df,"sepal width", "petal width", "Szerokość działki kielicha (cm)", "Szerokość płatka (cm)")
        #6th
        generujWykresKSrednich(centroidy,df,"petal length", "petal width", "Długość płatka (cm)", "Szerokość płatka (cm)")

    return dfToList



def generujWykresKSrednich(centroidy, output,xTableName,yTableName, xAxisTitle, yAxisTitle):
    fig, ax = plt.subplots()
    sameKolumny = ["sepal length", "sepal width", "petal length", "petal width", "cluster"]

    xCentroida = sameKolumny.index(xTableName)
    yCentroida = sameKolumny.index(yTableName)
    #Rysowanie punktów klastra
    colors = ['#e82727', '#8fe3c1', '#8fd4f7']  # Lista kolorów dla klastrów
    for cluster_number in output['cluster'].unique():
        cluster = output[output['cluster'] == cluster_number]
        ax.scatter(cluster[xTableName], cluster[yTableName], label=f'Cluster {cluster_number}',
                   color=colors[cluster_number])

    #Rysowanie centroidów
    for idx, centroid in enumerate(centroidy):
        ax.plot(centroid[xCentroida], centroid[yCentroida], 'X', color=colors[idx], markersize=10, markeredgecolor='black',
                label=f'Centroid {idx}')

    ax.set_xlabel(xAxisTitle, fontsize=14)
    ax.set_ylabel(yAxisTitle, fontsize=14)
    # Formatowanie osi X i Y, aby zawsze używały liczby zmiennoprzecinkowej z jednym miejscem po przecinku
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    zapiszWykres('wykres')
    plt.show()
def generujWykresWCSSIteracje(dane,x):
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = dane[0]
    y2 = dane[1]

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Wartość parametru K", fontsize=12)
    ax1.set_ylabel("Ilość Iteracji", fontsize=12)
    ax1.plot(x, y1, linewidth=2, color='#8fe3c1')
    ax1.scatter(x, y1, color='#8fe3c1')  # Dodanie kropek dla y1

    ax2 = ax1.twinx()
    ax2.set_ylabel("Wskażnik WCSS", fontsize=12)
    ax2.plot(x, y2, linewidth=2, color='#8fd4f7')
    ax2.scatter(x, y2, color='#8fd4f7')  # Dodanie kropek dla y2

    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    zapiszWykres('wykres')
    plt.show()
def liczWCSS(dane):
    WCSS_glowne = 0
    for dana in dane:

        punkt = dana[:4]
        centroid = dana[5]
        odlegloscPunktuOdCentroidu = obliczOdleglosc(punkt, centroid)
        WCSS_glowne += odlegloscPunktuOdCentroidu**2
    return WCSS_glowne


def inicjacjaCentroidow(dane, k):
    cecha1Max = cecha2Max = cecha3Max = cecha4Max = float(-9999)
    cecha1Min = cecha2Min = cecha3Min = cecha4Min = float(9999)
    for punkt in dane:
        #maksymalne
        cecha1Max = max(punkt[0], cecha1Max)
        cecha2Max = max(punkt[1], cecha2Max)
        cecha3Max = max(punkt[2], cecha3Max)
        cecha4Max = max(punkt[3], cecha4Max)
        #minimalne
        cecha1Min = min(punkt[0], cecha1Min)
        cecha2Min = min(punkt[1], cecha2Min)
        cecha3Min = min(punkt[2], cecha3Min)
        cecha4Min = min(punkt[3], cecha4Min)
    centroidy = []
    for i in range(k):
        centroidy.append([losowaWartosc(cecha1Max, cecha1Min), losowaWartosc(cecha2Max, cecha2Min), losowaWartosc(cecha3Max, cecha3Min), losowaWartosc(cecha4Max, cecha4Min)])
    return centroidy
def losowaWartosc(minimum, maximum):
    losowaWart = (maximum - minimum) * random.random() + minimum
    return losowaWart
def przypiszKlastry(dane, centroidy):
    klastry = []
    for punkt in dane:

        najmniejszaOdleglosc = 9999
        klaster = None
        for i in range(len(centroidy)):

            odleglosc = obliczOdleglosc(punkt, centroidy[i])

            if najmniejszaOdleglosc > odleglosc:
                najmniejszaOdleglosc = odleglosc
                klaster = i
        klastry.append(klaster)

    return klastry
def obliczOdleglosc(punkt1, punkt2):
    odleglosc = (punkt1[0] - punkt2[0]) ** 2 + (punkt1[1] - punkt2[1]) ** 2+ (punkt1[2] - punkt2[2]) ** 2+ (punkt1[3] - punkt2[3]) ** 2
    odleglosc = math.sqrt(odleglosc)
    return odleglosc
def aktualizacjaCentroidow(punkty, klastry, k):

    noweCentroidy = []
    liczbyWKlastrach = []
    for i in range(k):
        noweCentroidy.append([0,0,0,0])
        liczbyWKlastrach.append(0)
    for punkt, klaster in zip(punkty, klastry):

        noweCentroidy[klaster][0] += punkt[0]
        noweCentroidy[klaster][1] += punkt[1]
        noweCentroidy[klaster][2] += punkt[2]
        noweCentroidy[klaster][3] += punkt[3]
        liczbyWKlastrach[klaster] += 1

    for i, (cecha1,cecha2,cecha3,cecha4) in enumerate(noweCentroidy):
        #nie liczymy centroidow dla pustych klastrow
        if liczbyWKlastrach[i] != 0:
            noweCentroidy[i] =(cecha1 / liczbyWKlastrach[i], cecha2 / liczbyWKlastrach[i], cecha3 / liczbyWKlastrach[i], cecha4 / liczbyWKlastrach[i])

    return noweCentroidy
def warunekStopu(poprzedniePrzypisania, aktualnePrzypisania):
    return poprzedniePrzypisania == aktualnePrzypisania
def zapiszWykres(nazwa, rozszerzenie='.jpg', folder='./wykresy'):
    licznik = 1
    pelnaNazwa = f"{nazwa}{rozszerzenie}"

    while os.path.exists(os.path.join(folder, pelnaNazwa)):
        pelnaNazwa = f"{nazwa}_{licznik}{rozszerzenie}"
        licznik += 1
    plt.savefig(os.path.join(folder, pelnaNazwa))
    print(f"Zapisano wykres jako: {pelnaNazwa}")









#funkcje z poprzednich zadan
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