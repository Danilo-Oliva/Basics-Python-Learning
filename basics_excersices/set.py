lista1 = input("Ingrese nombres para la primera lista separado por una coma: ").split(",")
lista2 = input("Ingrese nombres para la segunda lista separado por una coma: ").split(",")

set1 = set(nombre.strip() for nombre in lista1)
set2 = set(nombre.strip() for nombre in lista2)

print("Mostrando lista")
print(f"Nombres en ambas listas: {set1 & set2}")       # Intersección
print(f"Nombres solo en la primera lista: {set1 - set2}")  # Diferencia
print(f"Nombres solo en la segunda lista: {set2 - set1}")  # Diferencia
print(f"Todos los nombres sin repetidos: {set1 | set2}") 