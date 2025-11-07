#nombre = input("¿Como te llamas? : ") #EL INPUT SIRVE PARA PEDIR VALORES POR TECLADO 
#print("Hola" , nombre , ":)")
#PEDIR VALORES: 
print ('CALCULADORA BASICA' , '----------------' , 'ELIJA UNA OPCION POR FAVOR : ' , sep = '\n\n')
print("1. suma ","2. resta","3. Multiplicacion","4. Division", sep = '\n\n')
user_opcion = int(input("Elige una opcion : "))


valor1 =int(input("Ahora digita un valor : "))
valor2= int(input("Digita otro valor : "))


if (user_opcion == 1):
    resultado = valor1 + valor2
    print("El resultado de la suma es : " , resultado)

elif (user_opcion == 2):
    resultado = valor1 - valor2
    print("El resultado de la resta es : " , resultado)
    
elif (user_opcion == 3): 
    resultado = valor1 * valor2 
    print("El resultado de la multiplicacion es : " , resultado)

elif (user_opcion == 4):
    if (valor2 == 0):
       print("NO PUEDES DIVIDIR POR CERO")
    else: 
        resultado = valor1 / valor2
        print("el valor de la divion es : " , resultado)



"""
cabe aclarar que al principio me estaba dando error porque no le estaba poniendo al 
principio el tipo de dato que es, asi que por eso puse el int al principio 

"""
