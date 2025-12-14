####################################
# ALUMNO: Roberto_Sanchez_Ortega   #
# CURSO: 25/26                     #
# TAREA: UD5_Tarea4                #
####################################

import CambiosRSO
import InterfazRSO

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Convertir Euros a Libras")
    print("2. Convertir Libras a Euros")
    print("3. Convertir Euros a Yenes")
    print("4. Convertir Yenes a Euros")
    print("5. Convertir Euros a Dólares")
    print("6. Convertir Dólares a Euros")
    print("0. Salir")

def main():
    opcion = None  
    while opcion != '0':  
        mostrar_menu() 
        opcion = InterfazINICIALES.leer_entero_mensaje("Elija una opción (0-6): ")

        if opcion == 0:
            print("Fin del programa.")
        elif opcion == 1:
            euros = InterfazINICIALES.leer_flotante_mensaje("Introduzca la cantidad de Euros: ")
            libras = CambiosINICIALES.euro_a_libra(euros)
            print(f"{euros} Euros son {libras:.2f} Libras")
        elif opcion == 2:
            libras = InterfazINICIALES.leer_flotante_mensaje("Introduzca la cantidad de Libras: ")
            euros = CambiosINICIALES.libra_a_euro(libras)
            print(f"{libras} Libras son {euros:.2f} Euros")
        elif opcion == 3:
            euros = InterfazINICIALES.leer_flotante_mensaje("Introduzca la cantidad de Euros: ")
            yenes = CambiosINICIALES.euro_a_yen(euros)
            print(f"{euros} Euros son {yenes:.2f} Yenes")
        elif opcion == 4:
            yenes = InterfazINICIALES.leer_flotante_mensaje("Introduzca la cantidad de Yenes: ")
            euros = CambiosINICIALES.yen_a_euro(yenes)
            print(f"{yenes} Yenes son {euros:.2f} Euros")
        elif opcion == 5:
            euros = InterfazINICIALES.leer_flotante_mensaje("Introduzca la cantidad de Euros: ")
            dolares = CambiosINICIALES.euro_a_dollar(euros)
            print(f"{euros} Euros son {dolares:.2f} Dólares")
        elif opcion == 6:
            dolares = InterfazINICIALES.leer_flotante_mensaje("Introduzca la cantidad de Dólares: ")
            euros = CambiosINICIALES.dollar_a_euro(dolares)
            print(f"{dolares} Dólares son {euros:.2f} Euros")
        else:
            print("La opción introducida no es correcta.")

main()
