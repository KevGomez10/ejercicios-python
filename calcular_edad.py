print("¡Hola! , voy a decirte cuantos años tendras en 10 años y si eres mayor de edad actualmente o no  :) ")
nombre = input("Por favor dime tu nombre primero :) : ")
edad = int(input("Ahora dime tu edad : "))

edad_10_años = edad + 10
print("Tu edad dentro de 10 años sera de : " , edad_10_años)

print("Ahora te dire si eres mayor de edad o no :)  ")
if (edad < 18):
    print("Eres menor de edad!!")
else: 
        print("Eres mayor de edad, felicidades :) ")

print("Gracias por usar mi programa" , nombre)

