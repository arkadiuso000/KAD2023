import math
import random
from matplotlib import ticker
import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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
    plt.xlabel('Liczba sąsiadów k')
    plt.ylabel('Dokładność [%]')
    plt.xticks(range(1, 16))
    plt.yticks(range(0, 110, 10))
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    save_unique_figure('wykres')
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
    plt.title('Dokładność w procentach dla różnych wartości k')
    plt.xlabel('Liczba sąsiadów k')
    plt.ylabel('Dokładność [%]')
    plt.xticks(range(1, 16))
    plt.yticks(range(0, 110, 10))
    plt.grid(axis='y', linestyle='--', linewidth=0.7)
    save_unique_figure('wykres')
    plt.show()

    print("Najlepsza wartość k:", najlepszeK)
    print("Macierz pomyłek dla najlepszego k:")
    print(macierzPomylekDlaNajlepszegoK)


# def kNajblizszychSasiadow(punkt, dane, kategorie, k):
#
#     dane = dane.copy()
#     kategorie = kategorie.copy()
#     if len(punkt) == 2:
#         dane = normalizujZbior(dane)
#     #problem remisu rozwiazujemy poprzez zwiekszenie k o 1
#     while True:
#         kategorieSasiadow = szukajSasiadow(punkt,dane,kategorie, k)
#         kategoria = najczestrzaWartosc(kategorieSasiadow)
#         if kategoria != None:
#             break
#         k += 1
#         if k >= len(dane[0]):
#             break
#     return kategoria
# def szukajSasiadow(punkt, dane, kategorie, k):
#
#     noweDane = []
#     for i in range(len(dane[0])):
#         porcjaDanych = []
#         for j in range(len(dane)):
#             porcjaDanych.append(dane[j][i])
#         noweDane.append(porcjaDanych)
#     dane = noweDane
#
#     liczbaWymiarow = len(punkt)
#
#     sasiedzi = []
#     kategorieSasiadow = []
#
#     for i in range(0, k):
#         idNajblizszegoSasiada = None
#         najkrotszyDystans = None
#
#         for j in range (0, len(dane)):
#             dystans = 0
#             for wymiar in range(0,liczbaWymiarow):
#
#                 dystans += (punkt[wymiar] - dane[j][wymiar])**2
#             dystans = math.sqrt(dystans)
#
#             if najkrotszyDystans == None:
#                 najkrotszyDystans = dystans
#                 idNajblizszegoSasiada = j
#             elif najkrotszyDystans > dystans:
#                 najkrotszyDystans = dystans
#                 idNajblizszegoSasiada = j
#
#         sasiedzi.append(dane[idNajblizszegoSasiada])
#         print(len(kategorie), idNajblizszegoSasiada)
#         kategorieSasiadow.append(kategorie[idNajblizszegoSasiada])
#
#         dane.remove(dane[idNajblizszegoSasiada])
#         kategorie.remove(kategorie[idNajblizszegoSasiada])
#     return kategorieSasiadow, sasiedzi
#
#
# def normalizujZbior(dane):
#     znormalizowaneX = []
#     znormalizowaneY = []
#     listaX = []
#     listaY = []
#     for i in range(len(dane)):
#         listaX.append(dane[i][0])
#         listaY.append(dane[i][1])
#
#
#     minimalnaWartoscX = wyznaczMinimum(listaX)
#     maksymalnaWartoscX = wyznaczMaksimum(listaX)
#     minimalnaWartoscY = wyznaczMinimum(listaY)
#     maksymalnaWartoscY = wyznaczMaksimum(listaY)
#
#     for i in range(len(dane)):
#         znormalizowaneX.append((listaX[i] - minimalnaWartoscX)/(maksymalnaWartoscX - minimalnaWartoscX))
#         znormalizowaneY.append((listaY[i] - minimalnaWartoscY)/(maksymalnaWartoscY - minimalnaWartoscY))
#     return [znormalizowaneX,znormalizowaneY]
# def zlaczZnormlizowaneZbiory(dane):
#     output = []
#     for i in range(len(dane[0])):
#         output.append([dane[0][i],dane[1][i]])
#     return output
# def najczestrzaWartosc(lista):
#     listaUnikalnych = []
#
#     for i in range(len(lista[0])):
#         if lista[0][i] not in listaUnikalnych:
#             listaUnikalnych.append(lista[0][i])
#     najczestrzaWartosc = ''
#     najwiekszaIlosc = None
#     for i in range(len(listaUnikalnych)):
#         ilosc = lista[0].count(listaUnikalnych[i])
#         if najwiekszaIlosc == None:
#             najwiekszaIlosc = ilosc
#             najczestrzaWartosc = listaUnikalnych[i]
#
#         elif najwiekszaIlosc  < ilosc:
#             najwiekszaIlosc = ilosc
#             najczestrzaWartosc = listaUnikalnych[i]
#         elif najwiekszaIlosc == ilosc:
#             najczestrzaWartosc = None
#     return najczestrzaWartosc
#

#zad 3 podpunkt 1
def kSrednich( k,daneDoWykresu,xTableName,yTableName, xAxisTitle, yAxisTitle,czyPokazacWykres=False):
    dane = daneDoWykresu[[xTableName,yTableName]].copy().values
    centroidy = inicjacjaCentroidow(dane, k)
    # print(centroidy)
    poprzedniePrzypisania = []
    iloscPetli = 0
    for i in range(k):
        poprzedniePrzypisania.append([0,0])
    while True:
        iloscPetli += 1

        klastry = przypiszKlastry(dane, centroidy)
        centroidy = aktualizacjaCentroidow(dane, klastry, k)

        aktualnePrzypisania = unikalneWartosci(klastry)
        # print("aktualnePrzupisania = {}\npoprzedniePrzypisania = {}".format(aktualnePrzypisania,poprzedniePrzypisania))
        if warunekStopu(poprzedniePrzypisania, aktualnePrzypisania):
            break
        else:
            poprzedniePrzypisania = aktualnePrzypisania

    WCSS = liczWCSS(dane,centroidy,klastry)
    noweDane = daneDoWykresu.copy()
    if czyPokazacWykres:
        noweDane.loc[:,'cluster'] = klastry
        generujWykresKSrednich(centroidy,noweDane,xTableName,yTableName, xAxisTitle,yAxisTitle)
    return [k,iloscPetli, WCSS]
def generujWykresKSrednich(centroidy, output,xTableName,yTableName, xAxisTitle, yAxisTitle):
    fig, ax = plt.subplots()

    #Rysowanie punktów klastra
    colors = ['#e82727', '#8fe3c1', '#8fd4f7']  # Lista kolorów dla klastrów
    for cluster_number in output['cluster'].unique():
        cluster = output[output['cluster'] == cluster_number]
        ax.scatter(cluster[xTableName], cluster[yTableName], label=f'Cluster {cluster_number}',
                   color=colors[cluster_number])

    #Rysowanie centroidów
    for idx, centroid in enumerate(centroidy):
        ax.plot(centroid[0], centroid[1], 'X', color=colors[idx], markersize=10, markeredgecolor='black',
                label=f'Centroid {idx}')

    ax.set_xlabel(xAxisTitle, fontsize=14)
    ax.set_ylabel(yAxisTitle, fontsize=14)
    # Formatowanie osi X i Y, aby zawsze używały liczby zmiennoprzecinkowej z jednym miejscem po przecinku
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    save_unique_figure('wykres')
    plt.show()
def generujWykresWCSSIteracje(dane):
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = dane[0]
    y2 = dane[1]

    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Wartość parametru K", fontsize=12)
    ax1.set_ylabel("Ilość Iteracji", fontsize=12)
    ax1.plot(x, y1, linewidth=2, color='#8fe3c1')

    ax2 = ax1.twinx()
    ax2.set_ylabel("Wskażnik WCSS", fontsize=12)
    ax2.plot(x, y2, linewidth=2, color='#8fd4f7')
    # fig.tight_layout()

    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    save_unique_figure('wykres')
    plt.show()
def liczWCSS(dane, centroidy, klastry):
    WCSS = 0
    for i in range(len(dane)):
        punkt = dane[i]
        klaster = klastry[i]
        centroid = centroidy[klaster]
        WCSS += obliczOdleglosc(centroid,punkt)
    return WCSS
def okrojDaneWCSS(dane):
    okrojoneIlosci = []
    okrojoneWCSS = []
    for i in range(2, 11):
        wartosciIlosciPetli = []
        wartosciWCSS = []
        for rekord in dane:
            if rekord[0] == i:
                wartosciIlosciPetli.append(rekord[1])
                wartosciWCSS.append(rekord[2])

        sredniaWartoscIlosciPetli = wyznaczSredniaArytmetyczna(wartosciIlosciPetli)
        sredniaWartoscWCSS = wyznaczSredniaArytmetyczna(wartosciWCSS)
        okrojoneIlosci.append(sredniaWartoscIlosciPetli)
        okrojoneWCSS.append(sredniaWartoscWCSS)
    return [okrojoneIlosci,okrojoneWCSS]
def unikalneWartosci(lista):
    output = []
    unikalne = list(set(lista))
    for unikalnaWartosc in unikalne:
        output.append([unikalnaWartosc, lista.count(unikalnaWartosc)])
    return output
def inicjacjaCentroidow(dane, k):
    xMax = yMax = float(-9999)
    xMin = yMin = float(9999)
    for punkt in dane:
        xMax = max(punkt[0], xMax)
        yMax = max(punkt[1], yMax)
        xMin = min(punkt[0], xMin)
        yMin = min(punkt[1], yMin)
    centroidy = []
    for i in range(k):
        centroidy.append([losowaWartosc(xMin, xMax), losowaWartosc(yMin, yMax)])
    return centroidy
def losowaWartosc(minimum, maximum):
    return (maximum - minimum) + minimum * random.random()
def przypiszKlastry(dane, centroidy):
    klastry = []
    for punkt in dane:
        najmniejszaOdleglosc = float('inf')
        klaster = None
        for i, centroid in enumerate(centroidy):
            odleglosc = obliczOdleglosc(punkt, centroid)
            if najmniejszaOdleglosc > odleglosc:
                najmniejszaOdleglosc = odleglosc
                klaster = i
        klastry.append(klaster)
    return klastry
def obliczOdleglosc(punkt1, punkt2):
    odleglosc = math.sqrt((punkt1[0] - punkt2[0]) ** 2 + (punkt1[1] - punkt2[1]) ** 2)
    return odleglosc
def aktualizacjaCentroidow(punkty, klastry, k):
    noweCentroidy = []
    liczbyWKlastrach = []
    for i in range(k):
        noweCentroidy.append([0,0])
        liczbyWKlastrach.append([0])
    for punkt, klaster in zip(punkty, klastry):

        noweCentroidy[klaster][0] += punkt[0]
        noweCentroidy[klaster][1] += punkt[1]
        liczbyWKlastrach[klaster][0] += 1

    for i, (x,y) in enumerate(noweCentroidy):
        #nie liczymy centroidow dla pustych klastrow
        if liczbyWKlastrach[i][0] != 0:
            noweCentroidy[i] =(x / liczbyWKlastrach[i][0], y / liczbyWKlastrach[i][0])

    return noweCentroidy
def warunekStopu(poprzedniePrzypisania, aktualnePrzypisania):
    return poprzedniePrzypisania == aktualnePrzypisania
def save_unique_figure(base_filename, extension='.jpg', directory='./wykresy'):
    counter = 1
    filename = f"{base_filename}{extension}"
    # Dodaj liczbę do nazwy pliku, jeśli plik już istnieje
    while os.path.exists(os.path.join(directory, filename)):
        filename = f"{base_filename}_{counter}{extension}"
        counter += 1

    # Tworzenie przykładowego wykresu do zapisania
    plt.figure()
    plt.plot([1, 2, 3], [4, 5, 6])  # Tutaj dodaj kod generujący wykres
    plt.close()  # Zamknij figurę po zapisaniu

    # Zapisanie wykresu z unikalną nazwą pliku
    plt.savefig(os.path.join(directory, filename))
    print(f"Zapisano wykres jako: {filename}")

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