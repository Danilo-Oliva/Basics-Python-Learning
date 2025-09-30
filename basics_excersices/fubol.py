import numpy as np
import pandas as pd

rg = np.random.default_rng(2)

datos = {
  "Puntos" : rg.integers(0, 31, 10),
  "Rebotes" : rg.integers(0, 16, 10),
  "Asistencias" : rg.integers(0, 11, 10)
}
tabla = pd.DataFrame(datos)
tabla["Eficiencia"] = tabla.sum(axis=1)
tabla.insert(0, "Jugadores", [f"Jugador {i + 1}" for i in range(len(tabla))])
print(tabla)

idx_max = tabla["Puntos"].idxmax()

mejor_jugador = tabla.loc[idx_max, "Jugadores"]
mejor_puntos = tabla.loc[idx_max, "Puntos"]
print(f"\nEl mejor jugador fue {mejor_jugador} con {mejor_puntos} puntos")

promedio_rebotes = tabla["Rebotes"].mean()
print(f"El promedio de rebotes fue: {promedio_rebotes}")