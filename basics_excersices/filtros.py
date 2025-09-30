import numpy as np
import pandas as pd

rg = np.random.default_rng(2)

edades = rg.integers(18, 61, 50)
salarios = edades * 1000 + rg.integers(-5000, 5000, 50)

df = pd.DataFrame({
  "Edad" : edades,
  "Salario" : salarios
})

personas = df[(df.Edad >= 30) & (df.Edad <= 40) & (df.Salario > 35000)]

print(df)
print("\n", personas)

df["Decada"] = (df["Edad"] // 10) * 10
salario_x_edad = df.groupby("Decada")["Salario"].mean()
print(salario_x_edad)