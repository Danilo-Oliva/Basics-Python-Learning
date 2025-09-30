try:
  a = int(input("Ingrese un numero: "))
  b = int(input("Ingrese otro numero: "))
  if b == 0:
    raise ZeroDivisionError("No se puede dividir por 0")
  print(a/b)
except ValueError:
  print("Ingrese un numero valido")
except ZeroDivisionError as e:
  print(f"{e}")
finally:
  print("Finalizando programa...")