import myFunctions as mf
import matplotlib.pyplot as plt
import os
import numpy as np
myData = mf.importData("././Dane-20231111/data.csv")

# plt.figure(figsize=(16, 8))
plt.scatter(myData["sepal length"], myData["sepal width"], marker="p", )
# plt.yticks([2.0,2.5,3.0,3.5,4.0,4.5])
plt.xticks([4,5,6,7,8])
plt.show()