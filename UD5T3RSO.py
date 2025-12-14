####################################
# ALUMNO: Roberto_Sanchez_Ortega   #
# CURSO: 25/26                     #
# TAREA: UD5_Tarea3                #
####################################

productos = {
    "pan": 1.20,
    "leche": 0.99,
    "huevos": 2.50
}

def actualizar_producto():
    producto = input("Introduce el nombre del producto: ").strip().lower()  
    
    try:
        precio = float(input(f"Introduce el precio de '{producto}': "))
    except ValueError:
        print("El precio debe ser un número flotante válido.")
        return

    productos[producto] = precio
    
    print("\nDiccionario actualizado:")
    for prod, precio in productos.items():
        print(f"{prod.capitalize()}: {precio:.2f}")

actualizar_producto()
