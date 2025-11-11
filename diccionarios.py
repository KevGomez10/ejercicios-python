#diccionarios 
#los diccionarios almacenan datos en formato clave : valor, pensemos en ellos como una pequeña base de datos dentro del programa
persona = {
    "nombre" : "Kevin",
    "edad" : 23,
    "profesion" : "ingeniero"
}
print(persona["nombre"]) #muestra el valor que hay dentro de nombre
persona["edad"] = 24 #sirve para cambiar el valor 
persona ["pais"] = "colombia" #agregar clave nueva



"""
Los diccionarios en python son faciles de entender
funcionan con una clave y un valor, en este caso, dentro de persona, le pido que me muestr el valor de la clave persona 
"""
#Ejercicio practico 
#primero hay que definir el diccionario vacio
contacto = {}
print("Diccionario 'contacto' creado : " , contacto)


print ("Ingresa tus datos por favor : ")
nombre_usuario = input("Ingresa tu nombre : ")
edad_usuario = input("Ingresa tu edad : ")
correo_usuario = input("Ingresa tu correo : ")
ciudad_usuario = input("Ingresa el nombre de la ciudad en la que vives : ")

contacto["Nombre"] = nombre_usuario
contacto["edad"] = edad_usuario
contacto["correo"] = correo_usuario
contacto["ciudad"] = ciudad_usuario

print("\nDiccionario actualizado" , contacto)