####################################
# ALUMNO: Roberto_Sanchez_Ortega   #
# CURSO: 25/26                     #
# TAREA: UD5_Tarea4                #
####################################

import CambiosRSO

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Convertir Euros a Libras")
    print("2. Convertir Libras a Euros")
    print("3. Convertir Euros a Yenes")
    print("4. Convertir Yenes a Euros")
    print("0. Salir")

def leer_numero():
    numero = input()  
    try:
        numero = float(numero) 
        return numero 
    except ValueError:  
        print("Introduzca un número correcto.")
        return None  

def main():
    opcion = None 
    while opcion != '0':  
        mostrar_menu()  
        opcion = input("Elija una opción (0-4): ")

        if opcion == '0':
            print("Fin del programa.")
        elif opcion == '1':
            print("Introduzca la cantidad de Euros: ", end="")
            euros = leer_numero()
            if euros is not None:  
                libras = CambiosINICIALES.euro_a_libra(euros)
                print(f"{euros} Euros son {libras:.2f} Libras")
        elif opcion == '2':
            print("Introduzca la cantidad de Libras: ", end="")
            libras = leer_numero()
            if libras is not None: 
                euros = CambiosINICIALES.libra_a_euro(libras)
                print(f"{libras} Libras son {euros:.2f} Euros")
        elif opcion == '3':
            print("Introduzca la cantidad de Euros: ", end="")
            euros = leer_numero()
            if euros is not None: 
                yenes = CambiosINICIALES.euro_a_yen(euros)
                print(f"{euros} Euros son {yenes:.2f} Yenes")
        elif opcion == '4':
            print("Introduzca la cantidad de Yenes: ", end="")
            yenes = leer_numero()
            if yenes is not None: 
                euros = CambiosINICIALES.yen_a_euro(yenes)
                print(f"{yenes} Yenes son {euros:.2f} Euros")
        else:
            print("La opción introducida no es correcta.")

main()
