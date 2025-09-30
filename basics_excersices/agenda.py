agenda = {}

def agregarContacto():
  nombre = input("Ingrese nombre: ")
  edad = int(input("Ingrese edad: "))
  ciudad = input("Ingrese su ciudad: ")
  
  agenda[nombre] = {
    "edad" : edad,
    "ciudad" : ciudad
  }
  
def mostrarContacto():
  if not agenda:
    print("La agenda está vacia")
    return
  for nombre, datos in agenda.items():
    print(f"{nombre} -> Edad: {datos['edad']}, Ciudad: {datos['ciudad']}")
      
def buscarContacto():
  nombre = input("Ingrese nombre a buscar: ")
  if nombre in agenda:
    datos = agenda[nombre]
    print(f"{nombre} -> Edad: {datos['edad']}, Ciudad: {datos['ciudad']}")
  else:
    print("El nombre ingresado no se ha encontrado")

while True:
  print("-AGENDA PERSONAL-")
  print("1 - Agregar Contacto")
  print("2 - Mostrar Agenda")
  print("3 - Buscar Contacto")
  print("0 - Salir")
  opcion = int(input("Opcion: "))
  
  match opcion:
    case 1:
      agregarContacto()
    case 2: 
      mostrarContacto()
    case 3:
      buscarContacto()
    case 0:
      break
    case _:
      print("Opcion invalida")
      