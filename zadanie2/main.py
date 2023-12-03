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


#1st plot
#TODO
# czy dac tu podzialke jak w przykladzie czy nie?
mf.generatePlot(myData,"sepal length", "sepal width", "Długość działki kielicha (cm)","Szerokość dzialki kielicha (cm)",list(np.linspace(4.0,8.0,num=9)), list(np.linspace(2.0,4.5,num=6)))
plt.savefig('./wykresy/wykres1.jpg')
# plt.show()

#2nd plot
mf.generatePlot(myData, "sepal length", "petal length", "Długość działki kielicha (cm)", "Długość płatka (cm)",  list(np.linspace(4.0,8.0,num=9)), list(np.linspace(0,8.0,num=17)))
plt.savefig('./wykresy/wykres2.jpg')
# plt.show()

#3rd plot
mf.generatePlot(myData, "sepal length", "petal width", "Długość działki kielicha (cm)", "Szerokość płatka (cm)", list(np.linspace(4.0,8.0,num=9)),list(np.linspace(0,3.0,num=7)) )
plt.savefig('./wykresy/wykres3.jpg')
# plt.show()

#4th plot
mf.generatePlot(myData, "sepal width", "petal length", "Szerokość działki kielicha (cm)", "Długość płatka (cm)",  list(np.linspace(2.0,4.5,num=6)), list(np.linspace(0,7.0,num=15)))
plt.savefig('./wykresy/wykres4.jpg')
# plt.show()

#5th plot
mf.generatePlot(myData, "sepal width","petal width","Szerokość działki kielicha (cm)","Szerokość płatka (cm)",list(np.linspace(2.0,4.5,num=6)),list(np.linspace(0,2.5,num=6)))
plt.savefig('./wykresy/wykres5.jpg')
# plt.show()

#6th plot
mf.generatePlot(myData,"petal length","petal width","Długość płatka (cm)","Szerokość płatka (cm)", list(np.linspace(0.5,7.0,num=14)), list(np.linspace(0,2.5,num=6)))
plt.savefig('./wykresy/wykres6.jpg')
# plt.show()








# print("                     $*******$ Test funkcji $*******$")
# print("*** Test Wariancji ***\n")
# print("Petal len:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczWariancje(myData["petal length"]),np.var(myData["petal length"])))
# print("Sepal len:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczWariancje(myData["sepal length"]),np.var(myData["sepal length"])))
# print("Petal wid:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczWariancje(myData["petal width"]),np.var(myData["petal width"])))
# print("Sepal wid:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczWariancje(myData["sepal width"]),np.var(myData["sepal width"])))
#
# print("*** Test Odchylenia standardowego ***\n")
# print("Petal len:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczOdchylenieStandardowe(myData["petal length"]),np.std(myData["petal length"])))
# print("Sepal len:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczOdchylenieStandardowe(myData["sepal length"]),np.std(myData["sepal length"])))
# print("Petal wid:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczOdchylenieStandardowe(myData["petal width"]),np.std(myData["petal width"])))
# print("Sepal wid:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczOdchylenieStandardowe(myData["sepal width"]),np.std(myData["sepal width"])))
#
# print("*** Test Kowariancji ***\n")
# data1 = np.stack((myData["petal length"],myData["sepal length"]), axis=0)
# data2 = np.stack((myData["sepal length"],myData["petal width"]), axis=0)
# print("Petal len:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczKowariancje(myData["petal length"],myData["sepal length"]),np.cov(data1)[1][0]))
# print("Sepal len:\nMoja:    {} \nNumPy:   {}\n".format(mf.wyznaczKowariancje(myData["sepal length"],myData["petal width"]),np.cov(data2)[1][0]))


# plt.scatter(myData["sepal width"], myData["petal width"], marker="+", c="green" )
# plt.xticks()
plt.show()