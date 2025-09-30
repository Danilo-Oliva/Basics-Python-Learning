import operaciones as o

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))

print(f"Suma: {o.sumar(a,b)}")
print(f"Resta: {o.restar(a,b)}")
print(f"Multiplicación: {o.multiplicar(a,b)}")

try:
  print(f"Dividir: {o.dividir(a,b)}")
except ZeroDivisionError:
  print("No se puede dividir entre 0")
