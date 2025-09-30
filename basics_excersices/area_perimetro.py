def calcular_area_perimetro(altura, base):
  area = altura * base
  perimetro = 2 * (base + altura)
  return area, perimetro

altura = float(input("Ingrese altura: "))
base = float(input("Ingrese base: "))

a, p = calcular_area_perimetro(altura, base)

print(f"El area es: {a} y el perimetro es: {p}")