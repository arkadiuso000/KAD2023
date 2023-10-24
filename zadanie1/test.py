import numpy
import matlib
import statistics
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


columns = ["dlugosc dzialki kielicha", "szerokosc dzialki kielicha", "dlugosc platka", "szerokosc platka", "gatunek"]
myFile = pd.read_csv("././Dane-20231023/data.csv", header=None, names=columns)
