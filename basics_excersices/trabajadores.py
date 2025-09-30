import numpy as np
import pandas as pd

rg = np.random.default_rng(2)
sueldo = rg.integers(200000, 900000, 15)

tabla = pd.DataFrame(sueldo, columns=["Sueldo"])
tabla["Categoria"] = ["Alto" if s > 700000 else "Medio" if s <= 700000 and s >= 400000 else "Bajo" for s in tabla["Sueldo"]]
print(tabla)

sueldo_alto = tabla[tabla.loc[:, "Categoria"].str.contains("Alto")]
sueldo_medios = tabla[tabla.loc[:, "Categoria"].str.contains("Medio")]
sueldo_bajo = tabla[tabla.loc[:, "Categoria"].str.contains("Bajo")]

print(f"Cantidad de sueldos altos: {sueldo_alto.shape[0]}")
print(f"Cantidad de sueldos medios: {sueldo_medios.shape[0]}")
print(f"Cantidad de sueldos bajos: {sueldo_bajo.shape[0]}")