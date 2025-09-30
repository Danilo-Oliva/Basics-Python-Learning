import numpy as np
import pandas as pd

rg = np.random.default_rng(2)
ventas_diarias = rg.integers(100, 500, 30)

tabla = pd.DataFrame(ventas_diarias, columns=["Ventas"])

tabla.insert(0, "Dias", [i + 1 for i in range(len(tabla))])

primera_quin = tabla[tabla["Dias"] <= 15] ["Ventas"]
segunda_quin = tabla[tabla["Dias"] > 15] ["Ventas"]

prom_primera = primera_quin.mean()
prom_segunda = segunda_quin.mean()

idx_max = tabla["Ventas"].idxmax()
dia_max_venta = tabla.loc[idx_max, "Dias"]
max_venta = tabla.loc[idx_max, "Ventas"]

promedio = tabla["Ventas"].mean()
tabla["Categoría"] = ["Alta" if v > promedio else "Baja" for v in tabla["Ventas"]]

print(tabla)
print(f"\nEl promedio general fue de: {promedio}")
print(f"El promedio de la primera quincena fue de: {prom_primera}, el de la segunda fue de: {prom_segunda}")
print(f"El día con mayores ventas fue el: {dia_max_venta}, con {max_venta} ventas")