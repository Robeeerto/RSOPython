####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# TAREA: UD3_Tarea2                #
####################################
print("Entras en una habitación oscura con dos puertas:\n¿cuál abres, la puerta 1 o la puerta 2?: ")
opcion = int(input("Introduce tu opción: "))

if opcion == 1:
	print("Hay un oso gigante comiéndose una1 tarta de queso.")
	print("¿Qué haces?")
	print("1. Coger la tarta.")
	print("2. Gritarle al oso.")
	opcion = int(input("Introduce tu opción: "))
	
	if opcion == 1:
		print("El oso te come la cara.")
	elif opcion == 2:
		print("El oso huye, te comes la tarta y se abre una puerta de salida.")
	else:
		print("El oso te come las piernas.")
elif opcion == 2:
	print("Hay una mesa con tres consolas, ¿cuál enciendes?")
	print("1. Nintendo Switch con el Zelda.")
	print("2. MegaDrive con el Sonic.")
	print("3. PS5 con Hogwarts Legacy.")
	opcion = int(input("Introduce tu opción: "))

	if opcion == 1 or opcion == 3:
		print("Aparece el Dr. Robotnik y te fulmina con un rayo.")
	elif opcion == 2:
		print("En cuanto finalices Green Hill Zone se abre una puerta de salida.")
	else:
		print("Las consolas explotan y tu con ellas.")
else:
	print("Se abre una trampilla bajo el suelo y caes a un foso con un cartel que pone:\n\"CPIFP Alan Turing.\"")
