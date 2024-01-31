import math
import random
import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import copy
import matplotlib.pyplot as plt
from matplotlib import ticker



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
    plt.xlabel('Liczba sąsiadów k',fontsize=26)
    plt.ylabel('Dokładność [%]',fontsize=26)
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

    plt.xlabel('Liczba sąsiadów k',fontsize=26)
    plt.ylabel('Dokładność [%]',fontsize=26)
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

    df = pd.DataFrame(kopiaDanych, columns=columns)

    dfToList = df.values.tolist()

    if k==3:
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
    kolory = ['#e82727', '#8fe3c1', '#8fd4f7']  # Lista kolorów dla klastrów
    for numerKlastra in output['cluster'].unique():
        klaster = output[output['cluster'] == numerKlastra]
        ax.scatter(klaster[xTableName], klaster[yTableName], label=f'Cluster {numerKlastra}',
                   color=kolory[numerKlastra])

    #Rysowanie centroidów
    for indeks, centroid in enumerate(centroidy):
        ax.plot(centroid[xCentroida], centroid[yCentroida], 'X', color=kolory[indeks], markersize=10, markeredgecolor='black',
                label=f'Centroid {indeks}')

    ax.set_xlabel(xAxisTitle, fontsize=14)
    ax.set_ylabel(yAxisTitle, fontsize=14)
    # Formatowanie osi X i Y, aby zawsze używały liczby zmiennoprzecinkowej z jednym miejscem po przecinku
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    zapiszWykres('wykres')
    plt.show()
def generujWykresWCSSIteracje(iloscIteracji, wartoscWCSS):
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    fig, ax1 = plt.subplots(figsize=(8.55, 5))
    ax1.set_xlabel("Wartość parametru K", fontsize=12)
    ax1.set_ylabel("Ilość Iteracji", fontsize=12)
    line1, = ax1.plot(x, iloscIteracji, linewidth=2, color='#8fe3c1', label='Ilość Iteracji')
    ax1.scatter(x, iloscIteracji, color='#8fe3c1')

    ax2 = ax1.twinx()
    ax2.set_ylabel("Wskaźnik WCSS", fontsize=12)
    line2, = ax2.plot(x, wartoscWCSS, linewidth=2, color='#8fd4f7', label='Wskaźnik WCSS')
    ax2.scatter(x, wartoscWCSS, color='#8fd4f7')

    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))

    plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1)  # Dostosowanie marginesów
    fig.legend(handles=[line1, line2])
    zapiszWykres('wykres')
    plt.show()
def liczWCSS(dane):
    WCSS = 0
    for dana in dane:
        punkt = dana[:4]
        centroid = dana[5]
        odlegloscPunktuOdCentroidu = obliczOdleglosc(punkt, centroid)
        WCSS += odlegloscPunktuOdCentroidu**2
    return WCSS
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

            odleglosc = obliczOdleglosc(punkt, centroidy[i])**2

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




#funkcja, ktora ujednolica proces importowania danych
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
