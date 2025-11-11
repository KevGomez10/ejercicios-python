#tuplas
#las tuplas son como listas pero no se puede modificar 
#son utiles cuando se necesitan datos que no se deben cambiar, como por ejemplo dias de la semana: 
"""
dias = ("lunes" , "martes" , "miercoles" , "jueves" , "viernes")
print(dias[0]) #muesta lunes sisi
"""

colores = ()
cantidad_colores = 4
for i in range(cantidad_colores):
    nombre = input(f"Por favor, ingrese el nombre del color #{i+1} : ")
    colores.append(nombre)


opcion =int(input(" escribe un numero del 1 al 4 para saber que color es :  Digita el numero : "))
print(f"el nombre de la fruta que esta en la posicion {opcion} es {nombre}  ")