####################################
# ALUMNO: Roberto_Sánchez_Ortega   #
# CURSO: 25/26                     #
# TAREA: UD5_Tarea1                #
####################################

import CalculadoraRSO

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_opcion():
    try:
        opcion = int(input("Ingrese el número de la operación deseada (1-5): "))
        if 1 <= opcion <= 5:
            return opcion
        else:
            print("Por favor, ingrese un número entre 1 y 5.")
            return None
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return None

def obtener_datos():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("Entrada inválida. Debe ingresar números.")
        return None

def calcular():
    opcion = obtener_opcion()
    if opcion is None:
        return calcular()

    if opcion == 1:
        datos = obtener_datos()
        if datos:
            a, b = datos
            resultado = CalculadoraINICIALES.sumar(a, b)
            print(f"El resultado de la suma es: {resultado}")
    elif opcion == 2:
        datos = obtener_datos()
        if datos:
            a, b = datos
            resultado = CalculadoraINICIALES.restar(a, b)
            print(f"El resultado de la resta es: {resultado}")
    elif opcion == 3:
        datos = obtener_datos()
        if datos:
            a, b = datos
            resultado = CalculadoraINICIALES.multiplicar(a, b)
            print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        datos = obtener_datos()
        if datos:
            a, b = datos
            resultado = CalculadoraINICIALES.dividir(a, b)
            print(f"El resultado de la división es: {resultado}")
    elif opcion == 5:
        print("Saliendo de la calculadora...")

calcular()