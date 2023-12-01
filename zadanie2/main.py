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
#
# # plt.figure(figsize=(16, 8))
# plt.scatter(myData["sepal length"], myData["sepal width"], marker="+", )
# # plt.yticks([2.0,2.5,3.0,3.5,4.0,4.5])
# plt.xticks([4,5,6,7,8])
# plt.yticks([2.0,2.5,3.0,3.5,4.0,4.5])
# plt.xlabel("Długość działki kielicha (cm)")
# plt.ylabel("Szerokość dzialki kielicha (cm)")

#1st plot
mf.generatePlot(myData,"sepal length", "sepal width", "Długość działki kielicha (cm)","Szerokość dzialki kielicha (cm)","r = ...; y = ...",[4,5,6,7,8], [2.0,2.5,3.0,3.5,4.0,4.5])
plt.savefig('./wykresy/wykres1.jpg')
# plt.show()

#2nd plot
mf.generatePlot(myData, "sepal length", "petal length", "Długość działki kielicha (cm)", "Długość płatka (cm)", "r = ...; u = ...", list(np.linspace(4.0,8,num=9)), list(np.linspace(0,7.5,num=16)))
plt.savefig('./wykresy/wykres2.jpg')
plt.show()

#3rd plot
