import numpy as np
import matplotlib.pyplot as plt
import os
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

#tworzy folder
try:
    os.mkdir("./wykresy")
except FileExistsError:
    pass
#🤌

# PUNKT 3. - wykresy


nazwyWykresow = ["Długość działki kielicha", "Szerokość działki kielicha", "Długość płatka", "Szerokość płatka"]
        #dlugosc dzialki kielicha
#rozmiar calego obrazka
plt.figure(figsize=(16, 8))
#tworzy dwa wykresy na jednym obrazku
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

                        #rysowanie histogramu
axs[0].hist(myData[columns[0]], bins=np.arange(4, 8.5, 0.5), alpha=0.5, edgecolor='black', color='green')
#ustawia os x
# axs[0].set_xlim(4.0,8.0)

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
plt.savefig('./wykresy/wykres1.jpg')
plt.show()


        #szerokosc dzialki kielicha
#rozmiar calego obrazka
plt.figure(figsize=(16, 8))
#tworzy dwa wykresy na jednym obrazku
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

                        #rysowanie histogramu
axs[0].hist(myData[columns[1]], bins=np.arange(2.0, 4.75, 0.25), alpha=0.5, edgecolor='black', color='green')
#wlacza siatke
axs[0].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[0].set_ylabel('Liczebność',fontsize=16, fontweight='bold')
axs[0].set_xlabel('Szerokość (cm)',fontsize=16, fontweight='bold')
axs[0].set_title(nazwyWykresow[1],fontsize=16, fontweight='bold')

                        #rysowanie wykresu pudelkowego

#tworzy dane do wykresu
data1 = list(myData['species'].drop_duplicates())
data2 = [myData[myData['species'] == data1[0]]['sepal width'],
         myData[myData['species'] == data1[1]]['sepal width'],
         myData[myData['species'] == data1[2]]['sepal width']]
#oznaczenia na osi x

#wlacza siatke
axs[1].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[1].boxplot(data2, labels=data1,)
axs[1].set_ylabel('Szerokość (cm)', fontsize=16, fontweight='bold')
axs[1].set_xlabel("Gatunek", fontsize=16, fontweight='bold')


#zapewnia odpowiednie odstępy między wykresami
plt.tight_layout()
plt.savefig('./wykresy/wykres2.jpg')
plt.show()

        #dlugosc platka kielicha
#rozmiar calego obrazka
plt.figure(figsize=(16, 8))
#tworzy dwa wykresy na jednym obrazku
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

                        #rysowanie histogramu
axs[0].hist(myData[columns[2]], bins=np.arange(1.0, 8.0, 0.5), alpha=0.5, edgecolor='black', color='green')
#wlacza siatke
axs[0].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[0].set_ylabel('Liczebność',fontsize=16, fontweight='bold')
axs[0].set_xlabel('Długość (cm)',fontsize=16, fontweight='bold')
axs[0].set_title(nazwyWykresow[2],fontsize=16, fontweight='bold')

                        #rysowanie wykresu pudelkowego

#tworzy dane do wykresu
data1 = list(myData['species'].drop_duplicates())
data2 = [myData[myData['species'] == data1[0]]['petal length'],
         myData[myData['species'] == data1[1]]['petal length'],
         myData[myData['species'] == data1[2]]['petal length']]
#oznaczenia na osi x

#wlacza siatke
axs[1].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[1].boxplot(data2, labels=data1,)
axs[1].set_ylabel('Długość (cm)', fontsize=16, fontweight='bold')
axs[1].set_xlabel("Gatunek", fontsize=16, fontweight='bold')


#zapewnia odpowiednie odstępy między wykresami
plt.tight_layout()
plt.savefig('./wykresy/wykres3.jpg')
plt.show()


        #szerokosc platka kielicha
#rozmiar calego obrazka
plt.figure(figsize=(16, 8))
#tworzy dwa wykresy na jednym obrazku
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

                        #rysowanie histogramu
axs[0].hist(myData[columns[3]], bins=np.arange(0.0, 3.0, 0.25), alpha=0.5, edgecolor='black', color='green')
#wlacza siatke
axs[0].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[0].set_ylabel('Liczebność',fontsize=16, fontweight='bold')
axs[0].set_xlabel('Szerokość (cm)',fontsize=16, fontweight='bold')
axs[0].set_title(nazwyWykresow[2],fontsize=16, fontweight='bold')

                        #rysowanie wykresu pudelkowego

#tworzy dane do wykresu
data1 = list(myData['species'].drop_duplicates())
data2 = [myData[myData['species'] == data1[0]]['petal width'],
         myData[myData['species'] == data1[1]]['petal width'],
         myData[myData['species'] == data1[2]]['petal width']]
#oznaczenia na osi x

#wlacza siatke
axs[1].grid(True, linewidth=0.5)
#opisy z wlasciwosciami
axs[1].boxplot(data2, labels=data1,)
axs[1].set_ylabel('Szerokość (cm)', fontsize=16, fontweight='bold')
axs[1].set_xlabel("Gatunek", fontsize=16, fontweight='bold')


#zapewnia odpowiednie odstępy między wykresami
plt.tight_layout()
plt.savefig('./wykresy/wykres4.jpg')
plt.show()