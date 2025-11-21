#hoja para ver funciones en python
#programas organizados, modulares y reutilizables
# "Divide y vencerás" -- todo gran programa se contruye a partir de pequeñas piezas que trabajan juntas
#una funcion es un bloque de codigo que hace una tarea especifica
"""
def saludar():
    print("Hola mundo")
saludar() #llamada a la funcion
"""
#-----------------------------------------------------------------------------------------------------------------------------------

"""
#funciones con parametros
def sumar(a,b):
    resultado = a + b
    print(f"La suma es : {resultado}")
sumar(5,7)
#-----------------------------------------------------------------------------------------------------------------------------------


#funciones con retorno de valores
def multiplicar(x,y):
    return x * y    
prod = multiplicar(4,6)
print(f"El producto es : {prod}")

#-----------------------------------------------------------------------------------------------------------------------------------

#funciones con valores por defecto
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()
saludar("Kevin")

#-----------------------------------------------------------------------------------------------------------------------------------
#variables locales y globales
x = 10 #global
def mostrar():
    y = 5 #local
    print(f"Valor de x dentro de la funcion : {x}")
mostrar()
print(f"Valor de y dentro de la funcion : {y}")
#-----------------------------------------------------------------------------------------------------------------------------------
"""

#Ejercicio practico
def operaciones(a,b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b if b != 0 else "Indefinido (division por cero)"
    return suma, resta, multiplicar, dividir
res = operaciones(10,2)
print(f"Suma: {res[0]}, Resta: {res[1]}, Multiplicacion: {res[2]}, Division: {res[3]}")


#-----------------------------------------------------------------------------------------------------------------------------------
def es_par(num):
    return num % 2 == 0
numero = 12
if es_par(numero):
    print(f"{numero} es un numero par")
else:
    print(f"{numero} es un numero impar")
#-----------------------------------------------------------------------------------------------------------------------------------

def saludo_personalizado(nombre):
    print(f"Hola, {nombre}  Bienvenido/a!")
saludo_personalizado("Ana")
