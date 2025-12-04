####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# EJERCICIO: UD4_Tarea4            #
####################################

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'} 
d3 = {}

def unir_diccionarios(d1, d2):
    d3 = d1.copy()  # Crear una copia de d1
    d3.update(d2)   # Actualizar d3 con los elementos de d2
    return d3

d3 = unir_diccionarios(d1, d2)

print(d3)