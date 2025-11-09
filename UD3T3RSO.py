####################################
# ALUMNO: Roberto Sánchez Ortega   #
# CURSO: 25/26                     #
# TAREA: UD3_Tarea3                #
####################################
aeropuertos=[["AGP", "Málaga Costa del Sol"],
             ["SVQ", "Sevilla San Pablo"],
             ["MAD", "Madrid Barajas"],
             ["NRT", "Tokyo Narita"],
             ["HND", "Tokyo Haneda"],
             ["JFK", "New York John. F. Kennedy"]]
aeropuerto = input("Introduzca un código de aeropuerto: ").upper()

indice = 0

while indice < len(aeropuertos) and aeropuertos[indice][0] != aeropuerto:
    indice = indice + 1

if indice == len(aeropuertos):
    print(f"El código {aeropuerto} no corresponde a ningún aeropuerto")
else:
    print(f"El código {aeropuerto} corresponde al aeropuerto {aeropuertos[indice][1]}")
