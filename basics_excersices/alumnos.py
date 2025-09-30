import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rg = np.random.default_rng(2)

notas = rg.integers(1, 11, size=(10,4))

estudiantes = pd.DataFrame(notas, columns=["Matemáticas", "Historia", "Lengua", "Inglés"])

estudiantes["Promedio"] = estudiantes.mean(axis=1)
estudiantes.insert(0, "Alumno", [f"Alumno{i+1}" for i in range(len(estudiantes))])

print(estudiantes)

print("\f")
idx_max = estudiantes["Matemáticas"].idxmax()
mejor_alumno = estudiantes.loc[idx_max, "Alumno"]
mejor_nota = estudiantes.loc[idx_max, "Matemáticas"]

print(f"Alumno con mayor nota: {mejor_alumno} en Matemáticas: {mejor_nota}")