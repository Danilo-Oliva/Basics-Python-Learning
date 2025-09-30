import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rg = np.random.default_rng(2)

#Creo las ventas diarias
ventas_diarias = rg.integers(100, 501, size=(7,3))
print(ventas_diarias)

tabla = pd.DataFrame(ventas_diarias, columns=["Producto A", "Producto B", "Producto C"])

tabla["Total semana"] = tabla.sum(axis=1)

promedio = tabla[["Producto A", "Producto B", "Producto C"]].mean()

mejor_producto = promedio.idxmax()
mejor_promedio = promedio.max()

print(tabla)
print("Promedios:\n", promedio)
print(f"El mejor producto fue: {mejor_producto} con un promedio de: {mejor_promedio}")