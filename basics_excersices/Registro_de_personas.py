personas = []

while True :
  nombre  = input("Ingresa tu nombre: ")
  edad = int(input("Ingresa tu edad: "))
  ciudad = input("Ingresa tu ciudad: ")
  
  persona = {
    "nombre" : nombre,
    "edad" : edad,
    "ciudad" : ciudad
  }
  personas.append(persona)
  
  continuar = input("Desea continuar? (s/n): ")
  if continuar.lower() != 's':
    break
  
print("Personas registradas: \n")
  
for p in personas:
  estado = "Mayor de edad" if p["edad"] >= 18 else "Menor de edad"
  print(f"-{p['nombre']}, {p['edad']}, {p['ciudad']} ({estado})")