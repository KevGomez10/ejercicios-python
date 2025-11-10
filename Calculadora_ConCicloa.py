import os
os.system("cls" if os.name == "nt" else "clear")

print("Bienvenido a la calculadora que te va a permitir realizar las siguientes operaciones : ")
a = int(input("Digita un numero por favor : "))
b = int(input("Digita otro numero por favor : "))

while True:
    print("Que quieres hacer con este numero? : ")
    print('1. sumar' , '2.restas', '3.multiplicar' , '4.dividir' , '5.salir' , sep ='\n\n' )

    try:
        opcion = int(input("Digita una opcion (1,2,3,4 o 5 )"))
    except ValueError: 
        print("Error, por favor digita un numero : ")
        continue
    if (opcion == 1):
        resultado = a + b
        print(f"El resultado de {a} mas {b} es igual a {resultado}")
    elif(opcion == 2): 
        resultado = a - b
        print(f"El resultado de {a} menos {b} es igual a {resultado}")
    elif(opcion == 3):
        resultado = a * b 
        print(f"El resultado de {a} por {b} es igual a {resultado}")
    elif(opcion == 4):
        if b==0:
            print("no puedes dividir entre cero ")
        else:
            resultado = a / b
            print(f"El resultado de {a} divido {b} es igual a {resultado}")

    elif(opcion == 5):
        print("Gracias por utilizar el programa, Saliendo....")
        break
    else:
        print("Digita una opciona valida de nuevo : ")

      
 



        

        

    
