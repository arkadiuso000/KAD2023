
import math
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

# PUNKT 1.

# oblicza liczebność poszczególnych gatunków
liczebnosc_gatunkow = myData['species'].value_counts()
caloscLiczba = myData['species'].value_counts().sum()

# oblicza udział procentowy poszczególnych gatunków
# normalize=True oznacza ze chcemy wynik miec w procentach domyslnie jest false
udzial_procentowy = (myData['species'].value_counts(normalize=True) * 100).round(2)
calosProcent = (myData['species'].value_counts(normalize=True) * 100).sum()
print("\tPUNKT 1\n")
print("Liczebność poszczególnych gatunków:")
print(liczebnosc_gatunkow)
print("Razem: {}".format(caloscLiczba))
print("\nUdział procentowy poszczególnych gatunków [%]:")
print(udzial_procentowy)
print("Razem: {}".format(math.ceil(calosProcent)))

print("\n\n")
