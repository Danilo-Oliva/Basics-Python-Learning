import operaciones as op
from vehiculo import Auto, Moto

try:
  a = float(input("Ingrese un numero: "))
  b = float(input("Ingrese otro numero: "))
  
  print(f"Division: {op.dividir(a, b)}")
  print(f"Promedio de 10, 20, 30: {op.promediar(10, 20, 30)}")
  
  auto = Auto("Koenigsegg", "Jesko", 2)
  moto = Moto("Yamaha", "R3", 300)
  
  print(auto.mostrarInfo())
  print(moto.mostrarInfo())
  
except ValueError as e:
  print(f"Error de valor: {e}")
  
except ZeroDivisionError as e:
  print(f"Error matemático: {e}")

finally:
  print("Finalizando programa...")