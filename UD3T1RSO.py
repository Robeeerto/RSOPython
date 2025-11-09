####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# TAREA: UD3_Tarea1                #
####################################
curso = input("Por favor, introduzca un ciclo formativo del CPIFP Alan Turing: ").upper()
if curso == "SMR":
    print("Es un ciclo de grado medio")
elif curso == "DAM" or curso == "DAW":
    print("Es un ciclo de grado superior")
elif curso == "IABD" or curso == "CIBER" or curso == "VDRA":
    print("Es un curso de especialización") 
elif curso == "ASIR":
    print("Es el CFGS más joven del CPIFP Alan Turing")
else:
    print("Esta enseñanza no se imparte en el CPIFP Alan Turing")
