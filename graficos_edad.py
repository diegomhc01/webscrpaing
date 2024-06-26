import pandas as pd      # manejo de estructuras series y dataframes
from statistics import quantiles, mean
import matplotlib.pyplot as plt
import numpy as np 


width = 0.25  # the width of the bars
datos = pd.read_csv('edades_fallecimiento.csv', encoding='latin-1')

media = datos.mean()
ds = datos.std()

(unique, counts) = np.unique(datos, return_counts=True)

fig, ax = plt.subplots()
plt.hist(datos, color="black", ec="red", rwidth=0.8, alpha=0.5)
plt.title(f"Media {media.values} años \n Desviación estandar {ds.values}")
plt.xlabel('Edades')
plt.ylabel('Cantidad')
plt.grid(True)
plt.show()
