import pandas as pd
import numpy as np

rg = np.random.default_rng(2)
temperatura = rg.integers(5, 35, 30)

tabla = pd.DataFrame(temperatura, columns=["Temperatura"])

tabla.insert(0, "Dias", [f"Dia {f+1}" for f in range(len(tabla))])

tabla["Categoria"] = ["Calor" if t > 25 else "Templado" if t <= 25 and t >= 15 else "Frio" for t in tabla["Temperatura"]]

print(tabla)