####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# EJERCICIO: UD4_Tarea3            #
####################################

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None

def seleccionar_operacion():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    try:
        opcion = int(input("Ingrese el número de la operación: "))
        return opcion
    except ValueError:
        print("Error: Entrada no válida. Debe ingresar un número.")
        return None

def obtener_numero():
    correcto = False
    while not correcto:
        try:
            num = float(input("Ingrese un número: "))
            correcto = True
            return num
        except ValueError:
            print("Error: Entrada no válida. Debe ingresar un número.")

def calculadora():
    print("Bienvenido a la calculadora")

    opcion = seleccionar_operacion()

    while opcion in [1, 2, 3, 4]:
        num1 = obtener_numero()
        num2 = obtener_numero()

        if opcion == 1:
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == 4:
            resultado = dividir(num1, num2)
            if resultado is not None:
                print(f"Resultado: {resultado}")

        continuar = input("¿Desea realizar otra operación? (s/n): ").lower()

        if continuar == 's':
            opcion = seleccionar_operacion()
        else:
            print("Gracias por usar la calculadora.")
            return

calculadora()
