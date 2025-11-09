####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# TAREA: UD3_Tarea4                #
####################################

print("BIENVENIDO A LA CALCULADORA DE PYTHON")
print("0. Salir")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = int(input("Introduzca una opción: "))
while opcion != 0:

    if opcion == 1:
        numero1 = int(input("Introduzca el primer valor: "))
        numero2 = int(input("Introduzca el segundo valor: "))
        print(f"El resultado de sumar {numero1} más {numero2} es {numero1 + numero2}")
    elif opcion == 2:
        numero1 = int(input("Introduzca el primer valor: "))
        numero2 = int(input("Introduzca el segundo valor: "))
        print(f"El resultado de restar {numero1} menos {numero2} es {numero1 - numero2}")
    elif opcion == 3:
        numero1 = int(input("Introduzca el primer valor: "))
        numero2 = int(input("Introduzca el segundo valor: "))
        print(f"El resultado de multiplicar {numero1} por {numero2} es {numero1 * numero2}")
    elif opcion == 4:
        print("1. División entera")
        print("2. División flotante")
        opcion = int(input("Introduzca una opción: "))
        if opcion == 1:
            numero1 = int(input("Introduzca el primer valor: "))
            numero2 = int(input("Introduzca el segundo valor: "))
            print(f"El resultado de dividir {numero1} entre {numero2} es {numero1 // numero2} y el resto es {numero1 % numero2}")
        elif opcion == 2:
            numero1 = float(input("Introduzca el primer valor: "))
            numero2 = float(input("Introduzca el segundo valor: "))
            print(f"El resultado de dividir {numero1} entre {numero2} es {numero1 / numero2}")
        else:
            print("La opción introducida no es correcta")
    else:
        print("La opción introducida no es correcta")
    
    print("BIENVENIDO A LA CALCULADORA DE PYTHON")
    print("0. Sumar")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Introduzca una opción: "))
