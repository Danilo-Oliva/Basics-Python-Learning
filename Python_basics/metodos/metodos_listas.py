#list crea una lista
lista = list(["hola","soy","Danilo"])

#len devuelve la cantidad de elementos de una lista
resultado = len(lista)

#append agrega elementos  a la lista
lista.append("Lola")

#insert agrega elementos a la posicion de la lista que le indiquemos
lista.insert(3, "Oliva")

#extend agrega varios elementos en forma de lista a la lista
lista.extend(["Acosta", "Russo"])
print(lista)