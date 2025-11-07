print("Bienvenido al conversor de unidades")
print('Por favor ingresa una opcion y lo convertire tu valor de : ' , '1.Celsius a Fahremheit' , '2.Kilometros a millas' , '3.Metros a pies' , sep = '\n\n')
opcion = int(input("Ingresa la opcion que deseas  :) "))
valor = int(input("Ingresa el valor que quieres convertir : "))


if (opcion == 1  ):
    Fahrenheit = (valor * 9/5)+32 
    print("Digitaste" , valor , "Que en Fahremheit serian : " , Fahrenheit)

elif (opcion == 2):
     Millas = valor * 0.621371
     print("Digitaste" , valor , "KM que en millas serian " , Millas)

elif (opcion == 3):
    Pies = valor * 3.28084
    print("Digitaste" , valor , "metros que en pies serian")

else:
    print("Ingrese una opcion valida por favor : ") 
    
