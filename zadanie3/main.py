import myFunctions as mf
import matplotlib.pyplot as plt
import os
import numpy as np
#tworzy folder
try:
    #zabezpieczenie przed łindołsem
    os.mkdir(os.path.join(".", "wykresy"))
except FileExistsError:
    pass
#🤌
myData = mf.importData("././Dane-20231111/data.csv")

#flags
zad1Flaga = False

if zad1Flaga:
    daneWCSS = []
    for k in range(2,11):
        if k == 3:
            # 1st plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal length", "sepal width", "Długość działki kielicha (cm)",
                         "Szerokość dzialki kielicha (cm)", True))

            # 2nd plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal length", "petal length", "Długość działki kielicha (cm)", "Długość płatka (cm)",
                                         True))

            # 3rd plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal length", "petal width", "Długość działki kielicha (cm)", "Szerokość płatka (cm)",
                                         True))

            # 4th plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal width", "petal length", "Szerokość działki kielicha (cm)", "Długość płatka (cm)",
                                         True))

            # 5th plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal width", "petal width", "Szerokość działki kielicha (cm)",
                         "Szerokość płatka (cm)", True))

            # 6th plot
            daneWCSS.append(mf.kSrednich(k, myData, "petal length", "petal width", "Długość płatka (cm)", "Szerokość płatka (cm)", True))
        else:
            # 1st plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal length", "sepal width", "Długość działki kielicha (cm)",
                                          "Szerokość dzialki kielicha (cm)"))

            # 2nd plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal length", "petal length", "Długość działki kielicha (cm)",
                                          "Długość płatka (cm)"))

            # 3rd plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal length", "petal width", "Długość działki kielicha (cm)",
                                          "Szerokość płatka (cm)"))

            # 4th plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal width", "petal length", "Szerokość działki kielicha (cm)",
                                          "Długość płatka (cm)"))

            # 5th plot
            daneWCSS.append(mf.kSrednich(k, myData, "sepal width", "petal width", "Szerokość działki kielicha (cm)",
                                          "Szerokość płatka (cm)"))

            # 6th plot
            daneWCSS.append(
                mf.kSrednich(k, myData, "petal length", "petal width", "Długość płatka (cm)", "Szerokość płatka (cm)"))


    noweWCSS = mf.okrojDaneWCSS(daneWCSS)
    #7th wykres
    mf.generujWykresWCSSIteracje(noweWCSS)

dataTrain = mf.importData("././dane_train_test/data_train.csv")
dataTest = mf.importData("././dane_train_test/data_test.csv")

# print(dataTrain['species'].values.tolist())



# print(dataTrain[["sepal length", "sepal width"]].values.tolist())
# print(mf.znajdzSasiadow([5.5,4.1],dataTrain,"sepal length","sepal width",3))
dataTestAsList = dataTest[["sepal length","sepal width"]].values.tolist()
print(dataTestAsList)
a = mf.normalizujZbior(dataTestAsList)

znormalizonaDataTestAsList = mf.zlaczZnormlizowaneZbiory(a)
kategorie = dataTrain["species"].values.tolist()
kategorieTest = dataTest["species"].values.tolist()
print(len(kategorie),len(dataTestAsList))
przypasowania = []
for i in range(0,len(dataTest)):
    punkt = znormalizonaDataTestAsList[i]
    # output = mf.kNajblizszychSasiadow(punkt,dataTrain,"sepal length","sepal width",3)
    output = mf.kNajblizszychSasiadow(punkt,dataTrain[["sepal length","sepal width"]].values.tolist(),kategorie, 3)
    przypasowania.append(output)
    print(f"{i+1}. punkt: {punkt} | {kategorieTest[i]}, output: {output}")

print(przypasowania.count("setosa"))
print(przypasowania.count("virginica"))
print(przypasowania.count("versicolor"))