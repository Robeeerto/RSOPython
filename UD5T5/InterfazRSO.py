####################################
# ALUMNO: Roberto_Sanchez_Ortega   #
# CURSO: 25/26                     #
# TAREA: UD5_Tarea5                #
####################################

def leer_entero():
    numero = input() 
    while not numero.isdigit():  
        print("Introduzca un número correcto.")
        numero = input()  
    return int(numero) 

def leer_entero_mensaje(mensaje):
    print(mensaje, end="")
    return leer_entero()

def leer_flotante():
    numero = input()  
    try:
        return float(numero)  
    except ValueError: 
        print("Introduzca un número correcto.")
        return leer_flotante()  

def leer_flotante_mensaje(mensaje):
    print(mensaje, end="")
    return leer_flotante()
