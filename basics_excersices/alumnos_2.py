import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rg = np.random.default_rng(2)
notas = rg.integers(0, 10, size=(10, 5))

tabla = pd.DataFrame(notas, columns=["Matemática", "Historia", "Lengua", "Biología", "Inglés"])

tabla["Promedio"] = tabla.mean(axis = 1)

tabla.insert(0, "Alumnos", [f"Alumno {i+1}" for i in range(len(tabla))])

idx_max = tabla["Promedio"].idxmax()
mejor_alumno = tabla.loc[idx_max, "Alumnos"]
mejor_promedio = tabla.loc[idx_max, "Promedio"]
mejor_materia = tabla[["Matemática", "Historia", "Lengua", "Biología", "Inglés"]].mean().idxmax()

print(tabla)

print(f"\nEl mejor alumno fue: {mejor_alumno} con promedio de: {mejor_promedio}")
print(f"La materia con más promedio general fue: {mejor_materia}")

print(f"\nPromedio por materia:")
print(tabla[["Matemática", "Historia", "Lengua", "Biología", "Inglés"]].mean())


tabla[["Matemática", "Historia", "Lengua", "Biología", "Inglés"]].mean().plot(kind="bar")
plt.title("Promedio general por materia")
plt.ylabel("Nota promedio")
plt.show()
