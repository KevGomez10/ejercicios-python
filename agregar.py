agregar = {}
print("Diccionario 'agregar' creado : ", agregar)

# Bucle para añadir múltiples contactos
while True:
    print("\n--- Ingreso de Nuevo Contacto ---")
    
    # Pide los datos al usuario
    nombre = input("Ingresa el Nombre del contacto (o 'salir' para terminar): ").strip()

    # Condición de salida del bucle
    if nombre.lower() == 'salir':
        break
        
    edad = input(f"Ingresa la Edad de {nombre}: ").strip()
    correo = input(f"Ingresa el Correo de {nombre}: ").strip()
    
    # Usa el nombre como clave principal para almacenar los datos
    # Almacenamos los datos en un diccionario anidado, donde la clave es el nombre y el valor es otro diccionario
    agregar[nombre] = {
        "Edad": edad,''
        "Correo": correo
    }
    
    print(f"Contacto '{nombre}' añadido con éxito.")

print("\n--- Diccionario de Contactos ---")
print(agregar)

# --- Búsqueda de Contacto ---
if agregar: # Solo si hay contactos
    while True:
        print("\n--- Búsqueda de Contacto ---")
        clave_busqueda = input("Ingresa el NOMBRE del contacto que quieres ver (o 'finalizar' para salir): ").strip()
        
        if clave_busqueda.lower() == 'finalizar':
            break

        # Verifica si el nombre existe como clave principal
        if clave_busqueda in agregar:
            print(f"\nDatos de '{clave_busqueda}':")
            # Accedemos al diccionario anidado para obtener Edad y Correo
            print(f"  Edad: {agregar[clave_busqueda]['Edad']}")
            print(f"  Correo: {agregar[clave_busqueda]['Correo']}")
        else:
            print(f"El contacto con el nombre '{clave_busqueda}' no fue encontrado.")

# Salir del programa
input("\nPresiona Enter para finalizar...")