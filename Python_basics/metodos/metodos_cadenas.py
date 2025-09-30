cadena1 = "hola soy Danilo"
cadena2 = "1,2,3,4,5,6,7,8,9"

#dir devuelve todo lo que podemos hacer con el objeto que le enviamos
resultado = dir (cadena1) #esto es una funcion y no un metodo por eso se ponde el dir antes del objeto

#upper convierte todo a mayuscula
resultado = cadena1.upper()

#lower convierte todo a minuscula
resultado = cadena1.lower()

#capitalize convierte la primera letra en mayuscula y el resto en minuscula
resultado = cadena1.capitalize()

#find busca una cadena en otra cadena y devuelve la posicion en la que encuentra dicha cadena si no encuentra devuelve un -1
busqueda_find = cadena1.find("hola")

#index devuelve lo mismo que find, pero si no encuentra nada nos devuelve una excepcion
busqueda_find = cadena1.index("hola")

#isnumeric devuelve true si tu cadena es numerico
es_numerico = cadena2.isnumeric()

#isalpha devuelve true si tu cadena es alfanumerica, pero solo si no tiene espacios, ej: holasoydanilo
es_alphanumerico = cadena1.isalpha()

#cout cuenta las veces que se encontró una cadena dentro de otra cadena
contar_coincidencia = cadena1.count('a')

#len cuenta cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#starswith verifica si una cadena empieza con otra cadena dada
empieza_con = cadena1.startswith('h')

#endswith verifica si una cadena termina con otra cadena dada
termina_con = cadena1.endswith('o')

#replace reemplaza un pedazo de una cadena con otra cadena
cadena_nueva = cadena1.replace("Danilo","Lola")

#split separa cadenas con las cadenas dadas pero nos devuelve una lista, cada cadena va a ir con ''. Ej: 1,2,3,4,5,6,7,8,9 => '1','2','3','4', etc. Y le podemos pedir que nos muestre que tiene en determinada posicion dentro de la cadena. Ej: print(cadena_separada[1]) => 2
cadena_separada = cadena2.split(',')

print(cadena_separada)