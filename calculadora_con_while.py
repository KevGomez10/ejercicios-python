def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b


while True:
    print("\n1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '5':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break

    if opcion in ("1", "2", "3", "4"):
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(f"{a} + {b} = {sumar(a,b)}")
        elif opcion == '2':
            print(f"{a} - {b} = {restar(a,b)}")
        elif opcion == '3':
            print(f"{a} * {b} = {multiplicar(a,b)}")
        elif opcion == '4':
            print(f"{a} / {b} = {dividir(a,b)}")
    else:
        print("Opción inválida, intenta de nuevo.")
