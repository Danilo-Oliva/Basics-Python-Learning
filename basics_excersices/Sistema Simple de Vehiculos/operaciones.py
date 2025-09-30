def dividir(a, b):
  if b == 0:
    raise ZeroDivisionError("No se puede dividir por cero")
  return a / b
def promediar(*args):
  if len(args) == 0:
    raise ValueError("No se puede promediar sin ingreso de valores")
  return sum(args) / len(args)