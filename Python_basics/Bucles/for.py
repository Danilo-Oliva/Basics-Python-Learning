animales = ["gato","perro","loro","cocodrilo"]

for animal in animales:
  print(f'El animal es: {animal}')
  
numeros = [15,20,33,55]

#recorriendo la tupla junto a su indice
for num in enumerate(numeros):
  indice = num[0]
  valor = num[1]
  print(f'el indice es: {indice} y su valor es: {valor}')

tupla = ("Danilo","Fausto","Oliva")

for name in enumerate(tupla):
  nombre, segundo_nombre, apellido = tupla
  print(f'Su nombre es: {name}')
  
  #recorriendo la tupla pero salteando elementos
  frutas = ["banana","manzana","coco","higo","naranja","ciruela"]
  
  for fruta in frutas:
    if fruta == 'higo':
      continue
    print (f'me voy a comer las frutas: {fruta}')
    
    #rompiendo el bucle
    for fruta in frutas:
      print (f'voy a comer las frutas: {fruta}')
      if fruta == 'coco':
        break
    print ("Fin del bucle")