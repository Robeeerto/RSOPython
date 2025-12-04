####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# EJERCICIO: UD4_Tarea2            #
####################################
def liters_100km_to_miles_gallon(liters):
    mpg = 235.214583 / liters
    return mpg

def miles_gallon_to_liters_100km(miles):
    liters_100km = 235.214583 / miles
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))