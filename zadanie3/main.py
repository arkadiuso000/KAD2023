import myFunctions as mf

import pandas as pd
import os

#tworzy folder
try:
    #zabezpieczenie przed łindołsem
    os.mkdir(os.path.join(".", "wykresy"))
except FileExistsError:
    pass
#🤌
myData = mf.importData("././Dane-20231111/data.csv")
dataTrain = mf.importData("././dane_train_test/data_train.csv")
dataTest = mf.importData("././dane_train_test/data_test.csv")
#flags
podpunkt1Flag = True
podpunkt2Flag = False

if podpunkt1Flag:
    # Załadowanie pliku CSV
    df = pd.read_csv("././Dane-20231111/data.csv", header=None)

    # Wybór pierwszych czterech kolumn
    df_selected = df.iloc[:, :4]

    # Konwersja do listy list
    myNewData = df_selected.values.tolist()

    daneWCSS = []
    wartosciX = []

    for i in range(2, 11):
        output = mf.kSrednich(myNewData, i)
        daneWCSS.append(mf.liczWCSS(output))
        wartosciX.append(i)

    mf.generujWykresWCSSIteracje(mf.iteracje, daneWCSS)


if podpunkt2Flag:
    #8th plot
    mf.podpunkt2WszystkieCechy(dataTrain, dataTest)
    #9th plot
    mf.podpunkt2PoszczegolneCechy(dataTrain[["sepal length", "sepal width"]], dataTrain["species"], dataTest[["sepal length", "sepal width"]], dataTest["species"])
    #10th plot
    mf.podpunkt2PoszczegolneCechy(dataTrain[["sepal length", "petal length"]], dataTrain["species"], dataTest[["sepal length", "petal length"]], dataTest["species"])
    #11th plot
    mf.podpunkt2PoszczegolneCechy(dataTrain[["sepal length", "petal width"]], dataTrain["species"], dataTest[["sepal length", "petal width"]], dataTest["species"])
    #12th plot
    mf.podpunkt2PoszczegolneCechy(dataTrain[["sepal width", "petal length"]], dataTrain["species"], dataTest[["sepal width", "petal length"]], dataTest["species"])
    #13th
    mf.podpunkt2PoszczegolneCechy(dataTrain[["sepal width", "petal width"]], dataTrain["species"], dataTest[["sepal width", "petal width"]], dataTest["species"])
    #14th
    mf.podpunkt2PoszczegolneCechy(dataTrain[["petal length", "petal width"]], dataTrain["species"], dataTest[["petal length", "petal width"]], dataTest["species"])




