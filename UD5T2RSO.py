####################################
# ALUMNO: Roberto_Sanchez_Ortega   #
# CURSO: 25/26                     #
# TAREA: UD5_Tarea2                #
####################################

frutas_colores = {
    "manzana": "rojo",
    "plátano": "amarillo",
    "pera": "verde",
    "naranja": "naranja"
}

def buscar_fruta():
    fruta = input("Introduce el nombre de una fruta: ").lower()  
    if fruta in frutas_colores:
        print(f"El color del/la {fruta} es: {frutas_colores[fruta]}")
    else:
        print("Esa fruta no está en el diccionario.")

buscar_fruta()
