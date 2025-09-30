def Suma(*args):
  total = 0
  for n in args:
    total += n
  return total

while True:
  entrada = input("Ingrese numeros con espacios: ").strip().lower()
  if entrada == 'salir':
    break
  
  try:
    numeros = [float(num) for num in entrada.split()]
    resultado = Suma(*numeros)
    print(f"El resultado de la suma es: {resultado}")
  except ValueError:
    print("ERROR: ingrese solo numeros")
  