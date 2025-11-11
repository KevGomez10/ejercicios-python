#listas en python 
"""

Las listas en python son como cajitas en donde puedes guardar muchos elementos o valores en si y puedes acceder a ellos, puedes agrear mas elementos a 
dicha lista, eliminarlos o modificarlos

"""
"""
frutas = ["manzana" , "pera" , "banana"]
print(frutas[0]) #me muestra que elemento esta en la posicion 0, que en este caso seria manzana
print(frutas[1]) # muestra que elemento esta en la posicion 1 que en este caso seria pera 

#operaciones basicas 
frutas.append("naranja") #agrega un elemento al final de la lista
frutas.remove("pera") #elimina un elemento
frutas[0] = "sandia" #cambia el valor en la posicion 0
print(len(frutas)) #muestra cuantos elementos hay

#Recorriendo una lista con un bucle
for fruta in frutas
print("me gusta comer" , fruta) #para cada elemento de frutas utilizamos la variable fruta para poder añadirle la palabra 

"""
"""
1. pida al usuario que ingrese 5 nombres de frutas y los guarde en una lista
2. luego muestre la lista completa
3. finalmente, pida al usuariio una fruta para eliminarla de la lista
"""
"""
"""

print("Bienvenido a tu lista de frutas")
print("Vamos a añadir frutas en tu lista, inserta el nombre de la fruta que vamos a insertar : ")
#parte 1 pedir y guardar los 5 nombres
lista_frutas = []
cantidad_frutas = 5 #repetimos la accion 5 veces 
for i in range(cantidad_frutas):
    nombre = input(f"Por favor, ingrese el nombre de la fruta #{i+1} : ")
    lista_frutas.append(nombre) #utilizamos el append para poder guardar los datos en la lista de frutas

#parte 2 mostrar la lista completa
print("LISTA COMPLETA")
print("la lista de frutas actual es : " , lista_frutas)

#parte 3
print("ELIMINAR FRUTA")
fruta_a_eliminar = input("Escribe el nombre de la fruta que vas a eliminar por favor : ")
if (fruta_a_eliminar in lista_frutas):
    lista_frutas.remove(fruta_a_eliminar)
    print(f"{fruta_a_eliminar} eliminada con exito")
    print("Asi quedo tu lista : " , lista_frutas)
else : 
    print(f"La fruta {fruta_a_eliminar} no se encuentra en la lista o escribiste mal, intenta de nuevo por favor")
print("FIN DEL PROGRAMA")


