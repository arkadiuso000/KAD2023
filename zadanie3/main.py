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



a = myData[['sepal length', 'sepal width']].copy()
output = mf.kSrednich(a.values,3)

#zlaczylem dane
a.loc[:,'cluster'] = output

# Utwórz wykres rozproszenia, gdzie kolor zależy od przypisania do klastra
fig, ax = plt.subplots()
for cluster_number in a['cluster'].unique():
    cluster = a[a['cluster'] == cluster_number]
    ax.scatter(cluster['sepal length'], cluster['sepal width'], label=f'Cluster {cluster_number}')

# Ustaw etykiety i tytuł wykresu
ax.set_title('Klastry długości i szerokości działki kielicha')
ax.set_xlabel('Długość działki kielicha (cm)')
ax.set_ylabel('Szerokość działki kielicha (cm)')

# Dodaj legendę
ax.legend()

# Pokaż wykres
plt.show()