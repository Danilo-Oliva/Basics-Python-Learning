#creando una lista (se puede modificar)
lista= ["danilo oliva", "lola acosta", True, 1.60]

#creando una tupla (no se puede modificar), es con  parentesis
tupla= ("danilo oliva", "lola acosta", True, 1.60)

#esto es valido
lista[3] = "18"

#esto no es valido
#tupla[3] = "18"

#creando un conjunto (set), no se pueden acceder por su index = print (conjunto [1]), tampoco se puede repetir datos dentro de su index
conjunto = {"danilo oliva", "lola acosta", True, 1.60 }

#Creando un diccionario, es un diccionario porque muestra su index por nombre del elemento y no por su posicion = print (diccionario['nombre'])
diccionario = {
    'nombre_de_hombre' : "Danilo Oliva",
    'nombre_de_mujer' : "Lola Acosta",
    'estan_en_pareja' : True,
    'altura' : 1.60,
    'dato_duplicado' : "Danilo Oliva"
}