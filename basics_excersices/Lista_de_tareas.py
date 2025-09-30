#tareas = []
#tarea = input("Ingrese una tarea: ")
#tareas.append(tarea)
#print(tareas[0])

lista_tareas = []

def agregarTareas(lista_tareas):
  while True:
    tarea = input("Ingrese una tarea o salir: ")
    if tarea.lower() == "salir":
      break
    lista_tareas.append(tarea)
    
def mostrarTareas(lista_tareas):
  for t in lista_tareas:
    print(t)
    
while True:
  print("\nBienvenido a tu anotador de tareas")
  print("\n1 - Agregar Tarea")
  print("\n2 - Mostrar Tareas")
  print("\n0 - Salir")
  opcion = int(input("opcion: "))
  if opcion == 0:
    break
  match opcion:
    case 1:
      agregarTareas(lista_tareas)
    case 2:
      mostrarTareas(lista_tareas)
    case _:
      print("opción invalida")
