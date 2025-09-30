def age_verify(age):
  if age >= 18:
    return "Mayor de edad"
  else:
    return "Menor de edad"
  
while True:
  age = int(input("Ingrese su edad: "))

  print(age_verify(age))
  
  continuar = input("Desea ingresar otra edad?(s/n): ")
  if continuar.lower() != 's':
    break