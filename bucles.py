"""
#ejercicio 1 con la estructura de control while 
#Permite que un bloque de código se ejecute repetidamente mientras una condición específica sea Verdadera (True).

# 1. Entrada  (Pedir el número 'n')
n = int(input("Por favor, digita un número (n): "))

# 2. Inicialización de variables
# 'i' será nuestro contador (la variable que cambia en el bucle)
i = 1 
# 'suma_total' será nuestro acumulador (la pista que diste)
suma_total = 0 

# 3. El Bucle While: Repetir mientras el contador 'i' sea menor o igual a 'n'
while i <= n: 
    # A. Mostrar el número actual que estamos procesando
    print(i)
    
    # B. ACUMULACIÓN: Sumar el valor actual de 'i' al total
    suma_total = suma_total + i 
    
    # C. ACTUALIZACIÓN: Mover el contador hacia 'n' (para evitar el bucle infinito)
    i += 1 

# 4. Mostrar el resultado final (¡Fuera del bucle!)
# Las instrucciones finales se ejecutan SOLO una vez, cuando el bucle termina.
print("------------------------------")
print("La suma total de los números del 1 hasta", n, "es:", suma_total)
"""

#ejercicio 2 
# CÓDIGO CORREGIDO PARA TABLA DE MULTIPLICAR
"""
print("--- Tablas de multiplicar ---")

# 1. Capturar el número que el usuario quiere multiplicar (n)
n = int(input("Digita el número de la tabla que quieres generar (n): "))

# 2. Iterar usando el bucle 'for'
# Usamos 'i' como el contador para la multiplicación (1, 2, 3... 10).
# range(1, 11) genera números desde 1 (incluido) hasta 11 (excluido).
for i in range(1, 11):
    
    # 3. Realizar la operación en cada iteración
    resultado = n * i
    
    # 4. Imprimir la operación completa y el resultado
    # Usamos f-string para formatear la salida de forma clara: n x i = resultado
    print(f"{n} x {i} = {resultado}") 

print("--- Fin de la tabla ---")
"""

"""

n = int(input("Digita el nuemro de la tabla que quiers generar : "))
for i in range(1,11):
    multi = n * i 
    print(f"{n} X {i} = {multi}")




VAS A ENCONTRAR MUCHOS FOR PORQUE ES ALGO QUE ESTABA REPASANDO MUCHO ENTONCES ES POR ESO, EN ESTA HOJA POR DECIRLO ASI ESTAN LOS DOS BUCLES
WHILE Y FOR 


"""

"""
n = int(input("Por favor digita el numero de la tabla de multiplicar que deseas generar : "))
for i in range (1,11):
    resultado = n * i                                                                                                #ejercicio final 
    print(f"{n} x {i} = {resultado}")

"""
"""
La explicacion de este codigo y en general del bucle for es que la varible n es donde vamos a guardar el numero ingresado por teclado 
en el for vamos a utilizar una variable i que va a ser la que va a ir aumentado de 1 hasta el 10, luego de eso multiplicamos n x i y lo imprimimos 

"""


#tarea practica 
print ("Bienvenido, en este programa vas a poder hacer 2 cosas con el valor que me digas : ")
n = int(input("Por favor digita un numero (n) : "))
print('¿Que quieres hacer con este numero?' , '1. Ver tabla de multiplicar' , '2. Sumar todos los numeros hasta N' , '3. SALIR' , sep = '\n\n')
opcion = int(input('Digita un numero : '))
if (opcion == 1) : 
    for i in range (1,11):
        multi = n * i
        print (f"{n} X {i} = {multi} ")
elif(opcion == 2):
    i = 1
    suma_total = 0
    while i <= n: 
        print(i)
        suma_total = suma_total + i
        i += 1
    print("------------------------------")
    print("La suma total de los números del 1 hasta", n, "es:", suma_total)
elif (opcion == 3 ):
    print("Gracias por utilizar el programa :)")
    

     
    


